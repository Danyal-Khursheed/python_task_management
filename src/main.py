from fastapi import FastAPI, HTTPException

from src.schema.post import PostCreate

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "description": "Learn Python fundamentals",
    },
    {
        "id": 2,
        "title": "Learn FastAPI",
        "description": "Build APIs using FastAPI",
    },
    {
        "id": 3,
        "title": "Connect PostgreSQL",
        "description": "Integrate PostgreSQL with FastAPI",
    },
]


@app.get("/get-all-posts")
def get_all_posts(limit: int):
    if limit:
        return tasks[:limit]
    return tasks


@app.get("/get-single-post/{id}")
def get_single_post(id: int):
    for item in tasks:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/add-to-tasks")
def create_tasks(post: PostCreate):
    max_post_id = max(task["id"] for task in tasks)
    new_post_id = max_post_id + 1

    new_task = {
        "id": new_post_id,
        "title": post.title,
        "description": post.description,
    }
    tasks.append(new_task)
    return new_task
