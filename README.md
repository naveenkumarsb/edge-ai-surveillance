# 🛡️ Intelligent Secure Edge-AI Surveillance & Perimeter Security

> **A modular Edge-AI security platform for real-time visual monitoring, object tracking, restricted-zone detection, risk analysis, cybersecurity monitoring, and event-driven alerting.**
>
> The system is designed to process surveillance data locally where practical, converting camera activity into structured security events while providing a foundation for future edge deployment, analytics, and security operations.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-111111?style=for-the-badge)
![Edge AI](https://img.shields.io/badge/Edge%20AI-Local%20Inference-FF6F00?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Monitoring-D32F2F?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2EA44F?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-F0AD4E?style=for-the-badge)

</p>

---

## 🚀 Key Features

- **Real-Time Object Detection:** Processes live camera frames using an AI-based object detection pipeline.
- **Multi-Object Tracking:** Maintains object identities across consecutive frames.
- **Restricted-Zone Detection:** Defines security regions and detects objects entering monitored areas.
- **Spatial Security Analysis:** Evaluates object positions relative to configured security boundaries.
- **Risk Assessment:** Converts detected security events into contextual risk information.
- **Cybersecurity Monitoring:** Monitors host-level indicators such as CPU, memory, processes, and system health.
- **Event-Driven Architecture:** Separates continuous video processing from meaningful security events.
- **Alert Management:** Generates structured alerts with severity, object, zone, confidence, and timestamp information.
- **Event Logging:** Maintains structured security-event records for future analysis.
- **Edge-First Processing:** Supports local processing to reduce unnecessary transmission of sensitive camera data.
- **Modular Architecture:** Separates detection, tracking, risk analysis, cybersecurity, alerting, and logging into independent components.
- **Edge Deployment Ready:** Architecture can be extended toward Raspberry Pi, Jetson, FPGA, NPU, or other edge platforms.

---

## 🧠 System Architecture

```text
                         CAMERA INPUT
                              │
                              ▼
                    ┌───────────────────┐
                    │   Frame Capture   │
                    │      OpenCV       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Object Detector │
                    │     Edge AI       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Object Tracker   │
                    │ Persistent IDs     │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
       ┌───────────────────┐     ┌────────────────────┐
       │ Spatial Security  │     │ Cybersecurity      │
       │                   │     │ Monitor            │
       │ • Zones           │     │                    │
       │ • Intrusion       │     │ • CPU              │
       │ • Position        │     │ • Memory           │
       │ • Dwell Time      │     │ • Processes        │
       └─────────┬─────────┘     └──────────┬─────────┘
                 │                          │
                 └────────────┬─────────────┘
                              ▼
                    ┌───────────────────┐
                    │    Event Engine   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Risk Engine    │
                    │                   │
                    │ • Confidence      │
                    │ • Context         │
                    │ • Zone            │
                    │ • Duration        │
                    │ • Risk Score      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Alert Manager   │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌──────────────┐
             │ Event Logger│     │  Dashboard   │
             └─────────────┘     └──────────────┘
