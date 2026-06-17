# 🏢 Jini Empire — Control Plane

Welcome to the central core engine of **Jini Empire**. This is an autonomous, **Zero Human Company** infrastructure designed to automate SaaS orchestration from scratch to deployment on decentralized cloud networks.

---

## 🔄 End-to-End Autonomous Workflow

The entire ecosystem operates 100% programmatically without any human intervention, leveraging Supabase as the state machine, GitHub Actions/Scripts as the muscle, and decentralized compute for execution.

```text
  [ User / Request ]
          │
          ▼ (1. Insert Metadata)
   ┌──────────────┐
   │  Supabase    │ ◄────────────────────────────────────────┐
   │  State Brain │                                          │
   └──────┬───────┘                                          │
          │                                                  │
          ├──(2. Webhook / Poll)                             │ (5. Health / Status Sync)
          ▼                                                  ▼
┌──────────────────────────────────┐      ┌──────────────────────────────────┐
│   Machine 1: App Launcher        │      │   Machine 2: Jini Deployer       │
│ ──────────────────────────────── │      │ ──────────────────────────────── │
│  • Fetches Template & Metadata   │      │  • 24/7 Health Monitoring        │
│  • Compiles Docker Images        │      │  • Zero-Downtime Upgrades        │
│  • Deploys to Akash Network      │      │  • Auto-Scales Machine 1 Workers │
└─────────────────┬────────────────┘      └──────────────────────────────────┘
                  │
                  ▼ (3. Execute SDL Bidding)
        ┌──────────────────┐
        │  Akash Network   │ (4. App Goes Live!)
        │  Decentralized   | ───────────────► [ Active Tenant App URL ]
        └──────────────────┘
```

---

### ⚡ Live Project Directory Tree
```text
jini-launchpad-core/
├── .github/
│   └── workflows/
│       ├── factory-workflow.yml
│       └── supervisor-workflow.yml
├── .gitignore
├── factory.py    # Machine 1: Core Compiler & Registry Pusher
├── requirements.txt
└── templates/
    └── Dockerfile
```

---

## 🏃‍♂️ Step-by-Step Execution Sequence

### 📥 Phase 1: The Blueprint (Supabase Brain)
* **Metadata Entry:** When a customer requests a SaaS app, a new row is inserted into Supabase with configuration specs:
  ```json
  {
    "app_name": "my-portfolio-app",
    "template": "nextjs-blog-theme",
    "cpu_ram": "1CPU-2GB",
    "status": "pending"
  }
  ```
* **The Trigger:** Supabase instantly triggers an internal webhook or alerts **Machine 1** via a fast polling loop.

### 🏗️ Phase 2: App Building & Launching (Machine 1)
* **Locking State:** Machine 1 updates the row status to `building` to prevent race conditions from other workers.
* **The Code Build:** It injects user data into the requested template (e.g., Next.js) and compiles a production-ready Docker image.
* **Akash Network Fitment:** Machine 1 automatically generates an SDL (Stack Definition Language) file, submits it to the Akash Network marketplace, closes the cheapest hosting bid, and deploys the container.
* **Success Sync:** Once live, it writes the live application URL back to Supabase and marks the status as `live`.

### 🛡️ Phase 3: Maintain, Scale & Upgrade (Machine 2 Guardian)
* **Self-Healing:** Machine 2 continuously tracks the uptime of Machine 1 and all deployed tenant apps. If anything crashes, it triggers an automatic **Auto-Restart**.
* **Auto-Scaling:** If the pending queue in Supabase spikes unexpectedly, Machine 2 dynamically boots up 3-4 parallel clone workers of Machine 1 to clear the backlog, then tears them down to save costs.
* **Zero-Downtime Upgrades:** When you push new platform code to GitHub, Machine 2 processes the update and rolls it out to running apps smoothly without a single second of downtime.

---

* 🔄 Last Automated Sync: `2026-06-17 09:47:17` *

* 🎯 **In Short:** **Supabase** is the brain, **Machine 1** is the muscle that builds and launches, and **Machine 2** is the manager that keeps the empire alive, optimized, and scaling forever.*