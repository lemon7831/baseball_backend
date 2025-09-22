import os
import sys 

# GCS 設定
GCS_BUCKET_NAME = "baseball_storage"

# 外部 API 端點
POSE_API_URL = "https://mmpose-api-new-924124779607.europe-west1.run.app/pose_video"
BALL_API_URL = "https://base-ball-detect-api-1069614647348.us-east4.run.app/predict"


# 內部 API 端點
# POSE_API_URL = "http://localhost:8000/pose_video"
# BALL_API_URL = "http://localhost:8080/predict"


# --- Render PostgreSQL 資料庫 URL 的最佳實踐 ---
# 最佳實踐：從不將生產環境的機敏資訊 (如資料庫URL) 直接寫在程式碼中。
# 我們應該直接從部署環境 (Google Cloud) 的「環境變數」中讀取。
# 如果在環境中找不到這個變數，就讓應用程式直接啟動失敗並報錯，
# 這樣可以避免應用程式在設定錯誤的情況下運行。

try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError:
    # 當在 Google Cloud 環境中找不到名為 "DATABASE_URL" 的環境變數時，
    # 會印出這個錯誤訊息並停止程式，提醒您去設定它。
    print("錯誤：環境變數 'DATABASE_URL' 未設定。請在 Google Cloud 的服務設定中新增此變數。")
    sys.exit(1)