---
title: "pg_auto_failover - High Availability Manager"
slug: pg_auto_failover
type: project-page
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <h1>pg_auto_failover</h1>
      <p class="subtitle">Automated PostgreSQL high availability</p>
      <p>pg_auto_failover monitors PostgreSQL nodes and manages failover automatically using native PostgreSQL streaming replication. A clear, predictable HA model without complex external orchestration.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
        <a href="https://github.com/hapostgres/pg_auto_failover" class="btn btn-secondary" target="_blank">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2>What pg_auto_failover does</h2>
      <p class="subtitle">Automatic promotion with zero data loss</p>
      <p>pg_auto_failover runs a monitor that tracks the health of primary and standby nodes. When the primary fails, the monitor promotes the standby and reconfigures the cluster — no manual intervention, no data loss, no external dependencies.</p>
      <div class="value_props">
        <div class="value_prop">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <h3>Why it matters</h3>
          <p class="subtitle">Manual failover is slow and error-prone under pressure</p>
          <ul class="use_cases_list">
            <li>Primary failures happen at the worst possible time</li>
            <li>Manual promotion steps are risky when you're half-awake at 3am</li>
            <li>External tools add operational complexity and new failure modes</li>
            <li>pg_auto_failover uses PostgreSQL's own replication — nothing to learn, nothing to trust blindly</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-shield-halved"></i>
          <h3>Typical use cases</h3>
          <p class="subtitle">Where pg_auto_failover fits</p>
          <ul class="use_cases_list">
            <li>Production PostgreSQL clusters requiring HA without Patroni complexity</li>
            <li>Kubernetes deployments needing predictable failover</li>
            <li>Teams who want HA behaviour they can reason about and test</li>
            <li>On-premise and cloud environments alike</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-bolt"></i>
          <h3>Key capabilities</h3>
          <p class="subtitle">Built on PostgreSQL native features</p>
          <ul class="capabilities_list">
            <li>Automatic failover with synchronous replication</li>
            <li>Zero data loss on controlled failover</li>
            <li>Monitor node coordinates the cluster state machine</li>
            <li>Works with any number of standby nodes</li>
            <li>Simple CLI for setup and operations</li>
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
      <p>Current work focuses on PostgreSQL version compatibility, Kubernetes operator integration, stability improvements for edge cases in network partition scenarios, and documentation.</p>
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
      <h2>Get pg_auto_failover</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pg_auto_failover is open source and available as a PostgreSQL extension. Packages are available for Debian, Ubuntu, and RPM-based distributions, and a Docker image is provided.</p>
      <div class="buttons">
        <a href="https://github.com/hapostgres/pg_auto_failover" class="btn btn-secondary" target="_blank">GitHub</a>
        <a href="https://pg-auto-failover.readthedocs.io" class="btn btn-secondary" target="_blank">Documentation</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_support">
  <div class="wrapper">
    <div class="content">
      <h2>Support pg_auto_failover</h2>
      <p class="subtitle">Keep high availability reliable</p>
      <p>If pg_auto_failover protects your production PostgreSQL cluster, supporting its maintenance ensures continued compatibility, faster fixes, and confidence in the behaviour you depend on.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
      </div>
    </div>
  </div>
</section>
