import os

# GCS 設定
GCS_BUCKET_NAME = "baseball_storage"

# 外部 API 端點
POSE_API_URL = "https://mmpose-api-new-924124779607.europe-west1.run.app/pose_video"
BALL_API_URL = "https://base-ball-detect-api-1069614647348.us-east4.run.app/predict"

# Render PostgreSQL 資料庫 URL
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://baseballdb_ghbi_user:OSG1ZtbXbaR2lyYY5IyPeXZHnvgDMTAa@dpg-d38ef83e5dus73a3mic0-a.oregon-postgres.render.com/baseballdb_ghbi")

# LemonAPI
# POSE_API_URL = "http://localhost:8000/pose_video"
# BALL_API_URL = "http://localhost:8080/predict"
