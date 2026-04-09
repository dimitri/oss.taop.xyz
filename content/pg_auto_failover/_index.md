---
title: "pg_auto_failover - High Availability Manager"
slug: pg_auto_failover
---

<div class="project_header">
  <h2>Automatic Failover for PostgreSQL</h2>
  <p class="project_description">pg_auto_failover monitors PostgreSQL databases and automatically manages failover to maintain high availability. Built on PostgreSQL native features for zero data loss.</p>
  <div class="project_links">
    <a href="https://github.com/hapostgres/pg_auto_failover" class="btn" target="_blank"><i class="fa-brands fa-github"></i> GitHub</a>
    <a href="https://pg-auto-failover.readthedocs.io" class="btn" target="_blank"><i class="fa-solid fa-globe"></i> Documentation</a>
  </div>
</div>

<div class="project_content">
  <h3>Overview</h3>
  <p>pg_auto_failover is a service that monitors and manages failover for PostgreSQL. It coordinates replication between primary and secondary nodes and automatically promotes a standby when the primary fails.</p>
  
  <h3>Key Features</h3>
  <ul>
    <li><strong>Automatic failover:</strong> No manual intervention needed when primary fails</li>
    <li><strong>Zero data loss:</strong> Uses synchronous replication to ensure no data is lost</li>
    <li><strong>PostgreSQL native:</strong> Built on PostgreSQL's native streaming replication</li>
    <li><strong>Simple configuration:</strong> Easy to set up and maintain</li>
    <li><strong>Health monitoring:</strong> Continuous monitoring of both primary and standby</li>
  </ul>
  
  <h3>Architecture</h3>
  <ul>
    <li>PostgreSQL primary node</li>
    <li>PostgreSQL standby node(s)</li>
    <li>pg_auto_failover monitor (single node or cluster)</li>
    <li>Automatic promotion of standby on primary failure</li>
  </ul>
  
  <h3>Installation</h3>
  <pre><code># From source
git clone https://github.com/hapostgres/pg_auto_failover.git
cd pg_auto_failover
make</code></pre>
  
  <p>pg_auto_failover is also available as a package in many distributions.</p>
  
  <h3>Quick Example</h3>
  <pre><code># Create a formation
pg_autoctl create formation --formation ha --kind postgres --num-sync-standby 1

# Add nodes
pg_autoctl create node --hostname node1 --name node1
pg_autoctl create node --hostname node2 --name node2</code></pre>
  
  <h3>Support Options</h3>
  <p>Get professional support and maintenance for pg_auto_failover in your production environment.</p>
  <div class="support_cta">
    <a href="#subscribe" class="btn">Subscribe to Maintenance</a>
  </div>
</div>
