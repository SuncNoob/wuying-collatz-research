# AI Coding playbook

Roles: planner (`plan`) → builder (`implement`) → reviewer (`review`).

A `plan` task should include:

- `path`: file to create or modify, relative to the repo
- `content` or `body`: expected contents

The planner spawns an `implement` task and a `review` task that depends on it.
The reviewer fails the pipeline if the file or implement result is missing.

## Research attempts (`mode: research`)

Same three roles. Use this when the deliverable is a **research note**, not a canned file.

A research `plan` should include:

- `path`: usually `workspace/<topic>.md`
- `body`: the mathematical problem (e.g. Collatz / 科拉茨猜想)
- `mode`: `research`

The builder runs **`codex exec` on that Agentic Computer** (无影 gateway token). The note must contain:

```markdown
## 命题
## 已知结果
## 尝试
## 缺口
```

The reviewer fails if those headings are missing or the note is too short. Open conjectures must stay attempts: do not accept a write-up that pretends the problem is fully proved.

Optional: a sibling `.py` that checks a finite range and prints `OK`.
