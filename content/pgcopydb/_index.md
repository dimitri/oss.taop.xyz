---
title: "pgcopydb - Database Copy Tool"
slug: pgcopydb
type: project-page
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <h1>pgcopydb</h1>
      <p class="subtitle">Copy PostgreSQL databases with minimal downtime</p>
      <p>pgcopydb copies a PostgreSQL database to a target server using logical replication and parallel workers. Designed for production migrations and version upgrades where pg_dump downtime is unacceptable.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
        <a href="https://github.com/dimitri/pgcopydb" class="btn btn-secondary" target="_blank">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2>What pgcopydb does</h2>
      <p class="subtitle">Live database cloning with logical replication</p>
      <p>pgcopydb copies a PostgreSQL database from source to target while the source remains online. It uses logical replication to keep the target in sync and only requires a short maintenance window for the final cutover.</p>
      <div class="value_props">
        <div class="value_prop">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <h3>Why it matters</h3>
          <p class="subtitle">Database migrations are complex and risky</p>
          <ul class="use_cases_list">
            <li>pg_dump and pg_restore cause significant downtime on large databases</li>
            <li>Binary-incompatible versions and cross-cloud moves rule out streaming replication</li>
            <li>pgcopydb handles the full copy lifecycle with a short, predictable cutover window</li>
            <li>Built for edge cases: large objects, sequences, indexes, and constraints</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-route"></i>
          <h3>Typical use cases</h3>
          <p class="subtitle">Where pgcopydb fits</p>
          <ul class="use_cases_list">
            <li>PostgreSQL major version upgrades with minimal downtime</li>
            <li>Cloud-to-cloud or on-premise-to-cloud migrations</li>
            <li>Creating read replicas across incompatible versions</li>
            <li>Database cloning for staging and testing environments</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-bolt"></i>
          <h3>Key capabilities</h3>
          <p class="subtitle">Built for production databases</p>
          <ul class="capabilities_list">
            <li>Logical replication for live copy with change tracking</li>
            <li>Parallel workers for table data, indexes, and constraints</li>
            <li>Table and schema filtering</li>
            <li>Large object support</li>
            <li>Progress tracking and resume on failure</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section_focus">
  <div class="wrapper">
    <div class="content">
      <h2>Current focus</h2>
      <p class="subtitle">Active maintenance areas</p>
      <p>Current work focuses on logical replication performance, broader data type coverage, improved progress reporting, and PostgreSQL version compatibility across all supported major versions.</p>
    </div>
  </div>
</section>

<section class="section section_how">
  <div class="wrapper">
    <div class="content">
      <h2>How maintenance works</h2>
      <p class="subtitle">Queue, SLA, quarterly releases</p>
      <p>Work is prioritized through a queue. Supported users receive priority handling, with defined response times. Fixes and improvements are grouped and shipped in quarterly releases.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See support options</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_get">
  <div class="wrapper">
    <div class="content">
      <h2>Get pgcopydb</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pgcopydb is open source, actively developed, and available for Linux. Packages are available for Debian, Ubuntu, and RPM-based distributions.</p>
      <div class="buttons">
        <a href="https://github.com/dimitri/pgcopydb" class="btn btn-secondary" target="_blank">GitHub</a>
        <a href="https://pgcopydb.readthedocs.io/" class="btn btn-secondary" target="_blank">Documentation</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_support">
  <div class="wrapper">
    <div class="content">
      <h2>Support pgcopydb</h2>
      <p class="subtitle">Keep database copies reliable</p>
      <p>If pgcopydb is part of your migration or upgrade workflow, supporting its maintenance ensures faster fixes, continued compatibility, and long-term reliability when it matters most.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
      </div>
    </div>
  </div>
</section>
