# Mnkhal Industrial Monitoring Platform
## Plug-and-Play Device Monitoring for Manufacturing

### What is Mnkhal Platform?

Mnkhal platform is a cloud-based platform that connects your industrial devices to real-time dashboards with zero technical complexity. Simply install our connector, add your devices, and start monitoring.

## How It Works

```
[Your Devices] → Mnkhal Connector → Mnkhal Cloud → Your Dashboard
  (Factory)      (5-min install)     (We manage)    (Access anywhere)
```

## Prerequisites

### At Your Plant
- Industrial devices with network connectivity (Ethernet/WiFi)
- One edge computer or Raspberry Pi (we provide configuration)
- Internet connection

### What Mnkhal Provides
- Cloud MQTT broker (managed)
- Dashboard platform (pre-configured)
- Data storage and alerts
- Technical support

## Installation (Simple 3-Step Process)

### Step 1: Install Mnkhal Connector (5 minutes)

**We provide a pre-configured device connector:**

```bash
# Download Mnkhal installer
curl -O https://mnkhal.io/install.sh
chmod +x install.sh

# Run installer
sudo ./install.sh

# Enter your company code (provided after signup)
# Installer automatically configures MQTT connection
```

**What the connector does:**
- Reads data from your devices via IP
- Sends data securely to Mnkhal cloud
- Auto-reconnects if internet drops
- Runs in background 24/7

### Step 2: Sign Up & Add Devices

1. **Create account:** https://mnkhal.io/signup
2. **Add production line:**
   - Enter line name (e.g., "Coffee Filter Line 1")
   - Select location

3. **Add devices:**
   - Click "Add Device"
   - Enter device IP address (e.g., `192.168.1.100`)
   - Select device type (filter, sensor, PLC, etc.)
   - Click "Connect"

4. **Configure data points:**
   - Mnkhal auto-detects available sensors
   - Select which metrics to monitor (temperature, speed, quality, etc.)
   - Set refresh rate (1-60 seconds)

### Step 3: Select Dashboard

1. **Choose template:**
   - Coffee Processing Dashboard
   - Generic Manufacturing Dashboard
   - Custom Dashboard

2. **Configure alerts:**
   - Set thresholds (e.g., temperature > 80°C)
   - Choose notification method (email, SMS, Slack)
   - Define response rules

3. **Start monitoring:**
   - Dashboard updates in real-time
   - Access from anywhere: `https://app.mnkhal.io/your-company`

## Supported Devices

### Direct IP Connection
- Industrial PLCs (Siemens, Allen-Bradley, Modbus)
- IoT sensors with network interface
- Coffee bean filters (MK IIR-9, MK SVN-45)
- Custom devices with API/MQTT support

### Protocol Support
- MQTT (automatic)
- Modbus TCP
- OPC UA
- REST API
- Custom protocols (contact support)

## Dashboard Features

### Real-Time Monitoring
- Live sensor readings (1-second updates)
- Visual quality indicators
- Production counters
- Equipment status

### Historical Analysis
- Trend charts (hourly, daily, monthly)
- Export to CSV/PDF
- Performance comparison
- Downtime analysis

### Alerts & Notifications
- Automatic threshold alerts
- Predictive maintenance warnings
- Email/SMS/Slack notifications
- Alert history and logs

### Grafana Integration (Optional)
- Export data to your Grafana instance
- Custom visualizations
- Third-party tool integration

## Data Storage & Management

### Cloud Database (Managed by Mnkhal)
- **Time-series database:** Optimized for sensor data (InfluxDB/TimescaleDB)
- **Automatic backups:** Daily snapshots, 30-day retention
- **High availability:** 99.9% uptime guarantee
- **Scalable:** Handles millions of data points per day

### Data Retention

| Plan | Real-Time Storage | Historical Archive | Export Options |
|------|-------------------|-------------------|----------------|
| **Starter** | 3 months | 1 year | CSV, JSON |
| **Professional** | 1 year | 3 years | CSV, JSON, Parquet |
| **Enterprise** | 2 years | Unlimited | All formats + API |

### Data Access

**Query Your Data:**
- Dashboard interface (no SQL required)
- REST API for custom applications
- Export historical data anytime
- Scheduled reports (daily/weekly/monthly)

**Example API request:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://api.mnkhal.io/v1/data?device=filter-1&from=2025-01-01&to=2025-01-31"
```

**Data Format:**
```json
{
  "device": "filter-1",
  "timestamp": "2025-01-15T10:30:00Z",
  "temperature": 75.5,
  "speed": 1200,
  "quality_score": 98.2,
  "defects_detected": 3
}
```

### Storage Features

**Automatic Aggregation:**
- Raw data: 1-second resolution (recent data)
- 1-minute averages: Last 7 days
- 1-hour averages: Last 90 days
- Daily summaries: All historical data

**Data Export:**
- Bulk export via dashboard
- Automated daily backups to your S3/storage (Enterprise)
- Integration with BI tools (Tableau, Power BI)

**Compliance:**
- GDPR compliant
- Data encryption at rest (AES-256)
- Audit logs of all data access
- Custom retention policies available

## Industrial Benefits

### Zero IT Overhead
- No server management
- No software updates
- No database administration
- We handle everything

### Rapid Deployment
- 5-minute connector installation
- Add devices in 2 minutes each
- Live dashboard immediately
- No coding required

### Cost Savings
- **Reduce defects:** Real-time quality monitoring catches issues early
- **Prevent downtime:** Predictive alerts before equipment fails
- **Optimize production:** Data-driven decisions increase efficiency by 15-30%
- **Lower labor:** Eliminate manual data logging

### Scalability
- Add unlimited devices
- Monitor multiple plants from one dashboard
- Multi-user access with role permissions
- API for custom integrations

### Compliance Ready
- Automatic data logging
- Export compliance reports
- Audit trail of all changes
- Meet ISO/FDA requirements

## Security

- **Encrypted connection:** TLS 1.3 for all device communication
- **No open ports:** Outbound-only connector (firewall friendly)
- **Role-based access:** Control who sees what data
- **SOC 2 compliant:** Enterprise-grade security
- **Private cloud option:** For sensitive industries

## Network Requirements

### Minimal Setup
- Internet connection (1 Mbps minimum)
- Static local IPs for devices (or DHCP reservation)
- Outbound port 8883 allowed (HTTPS alternative: 443)

### No Complex Configuration
- No port forwarding
- No VPN setup
- No static public IP needed
- Works with corporate firewalls

## Example: Coffee Processing Plant

### Before Mnkhal
- Manual quality checks every 2 hours
- 3% defect rate (stones/leaves in beans)
- 2 hours/day downtime from unexpected failures
- No production data

### After Mnkhal (30 days)
- Real-time quality monitoring (100% coverage)
- 0.8% defect rate (alerts catch issues instantly)
- 20 minutes/day downtime (predictive maintenance)
- Data-driven optimization increased throughput 18%

**ROI:** Paid for itself in 6 weeks through reduced waste and downtime.

---

*Mnkhal Platform - Industrial monitoring made simple. Focus on production, we handle the technology.*
