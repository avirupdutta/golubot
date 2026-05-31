import json
import runpy
from pathlib import Path


def test_generator_emits_expected_artifacts(tmp_path, monkeypatch):
    monkeypatch.setenv("LANCELOT_EVAL_OUTPUT_DIR", str(tmp_path))

    runpy.run_path("scripts/generate_lancelot_eval.py", run_name="__main__")

    expected_files = {
        "questions.json",
        "questions.md",
        "lancelot_prompt.md",
        "verifier_rubric.md",
        "batches",
    }
    assert expected_files == {path.name for path in tmp_path.iterdir()}


def test_questions_json_has_100_unique_complete_questions(tmp_path, monkeypatch):
    monkeypatch.setenv("LANCELOT_EVAL_OUTPUT_DIR", str(tmp_path))

    runpy.run_path("scripts/generate_lancelot_eval.py", run_name="__main__")

    questions = json.loads((tmp_path / "questions.json").read_text())
    assert len(questions) == 100
    assert len({question["id"] for question in questions}) == 100
    assert [question["id"] for question in questions] == [
        f"LQ-{index:03d}" for index in range(1, 101)
    ]

    for question in questions:
        assert question["difficulty"] in {"easy", "medium", "hard", "expert"}
        assert question["category"] in {
            "onboarding",
            "identity",
            "roster",
            "payments",
            "worlds",
            "admin",
            "integrations",
            "open-questions",
            "cross-module",
        }
        assert question["expected_answer_style"] in {
            "fact",
            "comparison",
            "workflow",
            "conflict-resolution",
            "multi-hop-analysis",
        }
        assert question["question"].strip()


def test_question_difficulty_distribution_matches_plan(tmp_path, monkeypatch):
    monkeypatch.setenv("LANCELOT_EVAL_OUTPUT_DIR", str(tmp_path))

    runpy.run_path("scripts/generate_lancelot_eval.py", run_name="__main__")

    questions = json.loads((tmp_path / "questions.json").read_text())
    counts = {
        difficulty: sum(
            question["difficulty"] == difficulty for question in questions
        )
        for difficulty in {"easy", "medium", "hard", "expert"}
    }

    assert counts == {"easy": 20, "medium": 35, "hard": 30, "expert": 15}


def test_prompts_include_schema_and_grading_dimensions(tmp_path, monkeypatch):
    monkeypatch.setenv("LANCELOT_EVAL_OUTPUT_DIR", str(tmp_path))

    runpy.run_path("scripts/generate_lancelot_eval.py", run_name="__main__")

    lancelot_prompt = (tmp_path / "lancelot_prompt.md").read_text()
    verifier_rubric = (tmp_path / "verifier_rubric.md").read_text()

    assert '"question_id":"LQ-001"' in lancelot_prompt
    assert '"confidence":"high|medium|low"' in lancelot_prompt
    assert "strict JSONL" in lancelot_prompt

    for dimension in [
        "Factual accuracy",
        "Source grounding",
        "Completeness",
        "Ambiguity handling",
        "Format compliance",
    ]:
        assert dimension in verifier_rubric


def test_generator_emits_10_batch_prompts_with_complete_coverage(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("LANCELOT_EVAL_OUTPUT_DIR", str(tmp_path))

    runpy.run_path("scripts/generate_lancelot_eval.py", run_name="__main__")

    batch_dir = tmp_path / "batches"
    batch_files = sorted(batch_dir.glob("batch_*.md"))
    assert [path.name for path in batch_files] == [
        f"batch_{index:02d}_LQ-{start:03d}-LQ-{start + 9:03d}.md"
        for index, start in enumerate(range(1, 101, 10), start=1)
    ]

    seen_ids = []
    for batch_index, batch_file in enumerate(batch_files, start=1):
        text = batch_file.read_text()
        start = (batch_index - 1) * 10 + 1
        expected_ids = [f"LQ-{index:03d}" for index in range(start, start + 10)]

        assert "Answer only the questions in this batch" in text
        assert "strict JSONL" in text
        assert '"question_id":"LQ-001"' in text
        for question_id in expected_ids:
            assert f"{question_id}:" in text
            seen_ids.append(question_id)

    assert seen_ids == [f"LQ-{index:03d}" for index in range(1, 101)]
