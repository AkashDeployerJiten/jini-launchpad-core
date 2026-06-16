import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Project path aur settings
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(PROJECT_DIR, "README.md")

# Strict Infrastructure Filter List
IGNORE_LIST = [
    ".git", "venv", "__pycache__", "generate_readme.py", 
    ".DS_Store", "README.md", "supervisor.log"
]

is_updating = False

def generate_tree(dir_path, prefix="", is_inside_builds=False):
    """
    Folder ka structure clean tree format me generate karne ke liye.
    """
    tree_str = ""
    try:
        raw_items = sorted(os.listdir(dir_path))
    except Exception:
        return ""
        
    items = []
    for x in raw_items:
        if x in IGNORE_LIST or "_old_" in x:
            continue
        items.append(x)
        
    for index, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (index == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        comment = ""
        if item == "factory.py":
            comment = "    # Machine 1: Core Compiler & Registry Pusher"
        elif item == "supervisor.py":
            comment = "    # Machine 2: Health Monitor & Orchestrator Loop"
        elif item == "test_fire.py":
            comment = "    # Micro-SaaS Cloud Event Trigger"
        elif item == "builds":
            comment = "       # Tenant Live Application Containers"
        elif is_inside_builds:
            comment = "   [Active Tenant Container]"

        if os.path.isdir(path):
            tree_str += f"{prefix}{connector}{item}/\n" if item == "builds" else f"{prefix}{connector}{item}/{comment}\n"
            
            if item == "builds":
                new_prefix = prefix + ("    " if is_last else "│   ")
                tree_str += generate_tree(path, new_prefix, is_inside_builds=True)
            elif is_inside_builds:
                continue
            else:
                new_prefix = prefix + ("    " if is_last else "│   ")
                tree_str += generate_tree(path, new_prefix, is_inside_builds=False)
        else:
            if is_inside_builds:
                continue
            tree_str += f"{prefix}{connector}{item}{comment}\n"
            
    return tree_str

def update_readme():
    """README.md file ko safely overwrite karna bina kisi formatting crash ke"""
    global is_updating
    if is_updating:
        return
        
    is_updating = True
    print("🔄 Folder structure changed! Refreshing README.md...")
    
    folder_tree = generate_tree(PROJECT_DIR)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Safe List Construction to strictly avoid any Pyright Unterminated Block Bugs
    lines = [
        "# 🏢 Jini Empire — Control Plane",
        "",
        "Welcome to the central core engine of **Jini Empire**. This is an autonomous, **Zero Human Company** infrastructure designed to automate SaaS orchestration from scratch to deployment on decentralized cloud networks.",
        "",
        "---",
        "",
        "## 🔄 End-to-End Autonomous Workflow",
        "",
        "The entire ecosystem operates 100% programmatically without any human intervention, leveraging Supabase as the state machine, GitHub Actions/Scripts as the muscle, and decentralized compute for execution.",
        "",
        "```text",
        "  [ User / Request ]",
        "          │",
        "          ▼ (1. Insert Metadata)",
        "   ┌──────────────┐",
        "   │  Supabase    │ ◄────────────────────────────────────────┐",
        "   │  State Brain │                                          │",
        "   └──────┬───────┘                                          │",
        "          │                                                  │",
        "          ├──(2. Webhook / Poll)                             │ (5. Health / Status Sync)",
        "          ▼                                                  ▼",
        "┌──────────────────────────────────┐      ┌──────────────────────────────────┐",
        "│   Machine 1: App Launcher        │      │   Machine 2: Jini Deployer       │",
        "│ ──────────────────────────────── │      │ ──────────────────────────────── │",
        "│  • Fetches Template & Metadata   │      │  • 24/7 Health Monitoring        │",
        "│  • Compiles Docker Images        │      │  • Zero-Downtime Upgrades        │",
        "│  • Deploys to Akash Network      │      │  • Auto-Scales Machine 1 Workers │",
        "└─────────────────┬────────────────┘      └──────────────────────────────────┘",
        "                  │",
        "                  ▼ (3. Execute SDL Bidding)",
        "        ┌──────────────────┐",
        "        │  Akash Network   │ (4. App Goes Live!)",
        "        │  Decentralized   | ───────────────► [ Active Tenant App URL ]",
        "        └──────────────────┘",
        "```",
        "",
        "---",
        "",
        "### ⚡ Live Project Directory Tree",
        "```text",
        "Jini Control Plane/",
        folder_tree.strip("\n"),
        "```",
        "",
        "---",
        "",
        "## 🏃‍♂️ Step-by-Step Execution Sequence",
        "",
        "### 📥 Phase 1: The Blueprint (Supabase Brain)",
        "* **Metadata Entry:** When a customer requests a SaaS app, a new row is inserted into Supabase with configuration specs:",
        "  ```json",
        "  {",
        '    "app_name": "my-portfolio-app",',
        '    "template": "nextjs-blog-theme",',
        '    "cpu_ram": "1CPU-2GB",',
        '    "status": "pending"',
        "  }",
        "  ```",
        "* **The Trigger:** Supabase instantly triggers an internal webhook or alerts **Machine 1** via a fast polling loop.",
        "",
        "### 🏗️ Phase 2: App Building & Launching (Machine 1)",
        "* **Locking State:** Machine 1 updates the row status to `building` to prevent race conditions from other workers.",
        "* **The Code Build:** It injects user data into the requested template (e.g., Next.js) and compiles a production-ready Docker image.",
        "* **Akash Network Fitment:** Machine 1 automatically generates an SDL (Stack Definition Language) file, submits it to the Akash Network marketplace, closes the cheapest hosting bid, and deploys the container.",
        "* **Success Sync:** Once live, it writes the live application URL back to Supabase and marks the status as `live`.",
        "",
        "### 🛡️ Phase 3: Maintain, Scale & Upgrade (Machine 2 Guardian)",
        "* **Self-Healing:** Machine 2 continuously tracks the uptime of Machine 1 and all deployed tenant apps. If anything crashes, it triggers an automatic **Auto-Restart**.",
        "* **Auto-Scaling:** If the pending queue in Supabase spikes unexpectedly, Machine 2 dynamically boots up 3-4 parallel clone workers of Machine 1 to clear the backlog, then tears them down to save costs.",
        "* **Zero-Downtime Upgrades:** When you push new platform code to GitHub, Machine 2 processes the update and rolls it out to running apps smoothly without a single second of downtime.",
        "",
        "---",
        "",
        "## 📊 System Status Dashboard",
        "",
        "| Component | Status | Tech Stack / Engine | Cost (Free Tier Optimized) |",
        "| :--- | :--- | :--- | :--- |",
        "| **Central Database** | 🟢 Active | Supabase (State Management) | `$0 (Free Tier)` |",
        "| **Machine 1 (Factory)** | 🟢 Active | Python / GitHub Actions | `$0 (Automation Framework)` |",
        "| **Machine 2 (Deployer)** | 🟡 Idle | Watchdog / Orchestrator Loop | `$0 (Self-Healing Scripts)` |",
        "| **Compute Provider** | 🟢 Connected | Akash Network (Decentralized Cloud) | ~`$1-$2 / Month per live app` |",
        "",
        "---",
        f"* 🔄 Last Automated Sync: `{current_time}` *",
        "",
        "* 🎯 **In Short:** **Supabase** is the brain, **Machine 1** is the muscle that builds and launches, and **Machine 2** is the manager that keeps the empire alive, optimized, and scaling forever.*"
    ]
    
    readme_content = "\n".join(lines)
    
    try:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("✨ README.md successfully updated without compiler alerts!")
    except Exception as e:
        print(f"🚨 Failed to write to dashboard: {str(e)}")
    finally:
        time.sleep(0.5)
        is_updating = False

class RefreshHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
            
        base_name = os.path.basename(event.src_path)
        if base_name in IGNORE_LIST or "_old_" in event.src_path or "builds" in event.src_path:
            return
            
        update_readme()

if __name__ == "__main__":
    print("================================================================")
    print("🚀 Jini Control Plane: Auto-README Bot Operational...")
    print("================================================================")
    
    update_readme()
    
    event_handler = RefreshHandler()
    observer = Observer()
    observer.schedule(event_handler, path=PROJECT_DIR, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nHalting Auto-README engine threads...")
        observer.stop()
    observer.join()