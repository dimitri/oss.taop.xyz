---
title: "pgloader - Database Migration Tool"
slug: pgloader
---

<div class="project_header">
  <h2>Database Migration Made Simple</h2>
  <p class="project_description">pgloader loads data from various sources into PostgreSQL with automatic schema conversion and high-performance parallel loading.</p>
  <div class="project_links">
    <a href="https://github.com/dimitri/pgloader" class="btn" target="_blank"><i class="fa-brands fa-github"></i> GitHub</a>
    <a href="https://pgloader.io" class="btn" target="_blank"><i class="fa-solid fa-globe"></i> Documentation</a>
  </div>
</div>

<div class="project_content">
  <h3>Overview</h3>
  <p>pgloader is a tool for loading data into PostgreSQL. It supports multiple source databases including MySQL, SQLite, MS SQL Server, and Oracle. pgloader can either COPY from files or connect to a database directly.</p>
  
  <h3>Key Features</h3>
  <ul>
    <li><strong>Multi-source support:</strong> Migrate from MySQL, SQLite, MSSQL, Oracle, and more</li>
    <li><strong>Automatic schema conversion:</strong> pgloader automatically converts source schema to PostgreSQL</li>
    <li><strong>Type conversion:</strong> Automatic mapping of source data types to PostgreSQL types</li>
    <li><strong>Parallel loading:</strong> High-performance loading with concurrent workers</li>
    <li><strong>Data validation:</strong> Built-in data validation and error reporting</li>
  </ul>
  
  <h3>Supported Sources</h3>
  <ul>
    <li>MySQL / MariaDB</li>
    <li>SQLite</li>
    <li>MS SQL Server</li>
    <li>Oracle Database</li>
    <li>CSV files</li>
    <li>FIXED format files</li>
  </ul>
  
  <h3>Installation</h3>
  <pre><code># From source
git clone https://github.com/dimitri/pgloader.git
cd pgloader
make</code></pre>
  
  <p>pgloader is also available as a Docker image:</p>
  <pre><code>docker pull dimitri/pgloader</code></pre>
  
  <h3>Quick Example</h3>
  <pre><code>pgloader mysql://user:password@host/dbname postgresql://user:password@localhost/dbname</code></pre>
  
  <h3>Support Options</h3>
  <p>Get professional support and maintenance for pgloader in your production environment.</p>
  <div class="support_cta">
    <a href="#subscribe" class="btn">Subscribe to Maintenance</a>
  </div>
</div>
