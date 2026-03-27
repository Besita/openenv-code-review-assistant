from envs.code_review_env import CodeReviewEnv

def main():
    env = CodeReviewEnv()
    print("✅ Code Review Environment Server Running")

    # simple test run
    obs = env.reset("easy")
    print("Sample task loaded:", obs.task_id)

# 🔥 REQUIRED for OpenEnv
if __name__ == "__main__":
    main()