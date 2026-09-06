---
title: "pg_auto_failover Maintenance and Priority Support"
slug: pg_auto_failover
type: project-page
description: "Funded maintenance for pg_auto_failover, automated PostgreSQL high availability built on native streaming replication — priority issue handling, SLAs, and quarterly releases."
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <p class="hero-kicker">Funded upstream maintenance</p>
      <h1>pg_auto_failover Maintenance and Priority Support</h1>
      <p class="subtitle">Automated PostgreSQL high availability, without an external consensus cluster to babysit</p>
      <p>pg_auto_failover runs a monitor that tracks the health of primary and standby nodes, promotes a standby when the primary fails, and reconfigures the cluster on its own. It is built on PostgreSQL&rsquo;s own replication, which is what keeps its behaviour something you can reason about and test rather than trust blindly.</p>
      <div class="hero-proof">
        <span><b>1,362</b>GitHub stars</span>
        <span><b>v2.2</b>Apr 2025</span>
        <span><b>2</b>vendors ship it as a documented HA option</span>
      </div>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="https://github.com/hapostgres/pg_auto_failover" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2 class="h-lead"><i class="fa-solid fa-heart-pulse section-icon"></i>What pg_auto_failover Does During a Failure</h2>
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
      <h2><i class="fa-solid fa-code-branch section-icon"></i>What&rsquo;s Being Worked On Right Now</h2>
      <p class="subtitle">Active maintenance areas</p>
      <p>Current work focuses on PostgreSQL version compatibility, Kubernetes operator integration, stability improvements for edge cases in network partition scenarios, and documentation.</p>
      <p>The full backlog for this project — last release, what has
      merged since, and the big features queued behind it — is on the
      <a href="/roadmap/#pg_auto_failover">roadmap page</a>, kept current rather than
      summarised here.</p>
    </div>
  </div>
</section>

<section class="section section_get">
  <div class="wrapper">
    <div class="content">
      <h2><i class="fa-solid fa-download section-icon"></i>Install pg_auto_failover</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pg_auto_failover is open source and available as a PostgreSQL extension. Packages are available for Debian, Ubuntu, and RPM-based distributions, and a Docker image is provided.</p>
      <p>The <a href="https://pg-auto-failover.readthedocs.io/" target="_blank" rel="noopener">pg_auto_failover documentation</a> covers the state machine, multi-standby setups, and the operations CLI.</p>
      <div class="buttons">
        <a href="https://github.com/hapostgres/pg_auto_failover" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
        <a href="https://pg-auto-failover.readthedocs.io" class="btn btn-secondary" target="_blank">Documentation</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_cta">
  <div class="wrapper">
    <div class="content">
      <h2>Fund pg_auto_failover Maintenance</h2>
      <p class="subtitle">Keep your HA setup supported through PostgreSQL upgrades</p>
      <p>VMware/Broadcom Tanzu Postgres documents pg_auto_failover as an officially supported HA option, and Microsoft&rsquo;s Citus Data is where it was born. HA software earns its keep on the day it fails over; funding its maintenance is what keeps that day boring, and what keeps compatibility current as PostgreSQL majors ship.</p>
      <p>Work is prioritized through one queue across all four projects,
      triaged against your tier&rsquo;s SLA, and shipped in quarterly
      releases &mdash; upstream, open source, for everyone.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="/roadmap/#pg_auto_failover" class="btn btn-secondary">See This Project&rsquo;s Backlog</a>
      </div>
    </div>
  </div>
</section>
