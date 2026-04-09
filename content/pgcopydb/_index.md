---
title: "pgcopydb - Database Copy Tool"
slug: pgcopydb
---

<div class="project_header">
  <h2>Copy PostgreSQL Databases with Minimal Downtime</h2>
  <p class="project_description">pgcopydb copies a PostgreSQL database to a target server. It uses logical replication for live copies and supports large databases with minimal downtime.</p>
  <div class="project_links">
    <a href="https://github.com/dimitri/pgcopydb" class="btn" target="_blank"><i class="fa-brands fa-github"></i> GitHub</a>
    <a href="https://pgcopydb.org" class="btn" target="_blank"><i class="fa-solid fa-globe"></i> Documentation</a>
  </div>
</div>

<div class="project_content">
  <h3>Overview</h3>
  <p>pgcopydb is a tool that helps you copy a PostgreSQL database from one server to another. Unlike simple pg_dump/pg_restore, pgcopydb is designed for production use with features like live replication and incremental copy.</p>
  
  <h3>Key Features</h3>
  <ul>
    <li><strong>Live database cloning:</strong> Copy data while the source database is online</li>
    <li><strong>Logical replication:</strong> Uses PostgreSQL's logical replication for efficiency</li>
    <li><strong>Minimal downtime:</strong> Only a short maintenance window needed</li>
    <li><strong>Large database support:</strong> Handles databases of any size</li>
    <li><strong>Table filtering:</strong> Copy only specific tables or schemas</li>
  </ul>
  
  <h3>Use Cases</h3>
  <ul>
    <li>Database migration to a new server</li>
    <li>Creating read replicas</li>
    <li>Database cloning for testing</li>
    <li>Upgrading to a new PostgreSQL version</li>
    <li>Moving to cloud PostgreSQL</li>
  </ul>
  
  <h3>Installation</h3>
  <pre><code># From source
git clone https://github.com/dimitri/pgcopydb.git
cd pgcopydb
make</code></pre>
  
  <p>pgcopydb is also available as a Docker image:</p>
  <pre><code>docker pull dimitri/pgcopydb</code></pre>
  
  <h3>Quick Example</h3>
  <pre><code>pgcopydb copy --source "postgres://source:5432/db" --target "postgres://target:5432/db"</code></pre>
  
  <h3>Support Options</h3>
  <p>Get professional support and maintenance for pgcopydb in your production environment.</p>
  <div class="support_cta">
    <a href="#subscribe" class="btn">Subscribe to Maintenance</a>
  </div>
</div>
