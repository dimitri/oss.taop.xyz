---
title: "pgcopydb Maintenance and Priority Support"
slug: pgcopydb
type: project-page
description: "Funded maintenance for pgcopydb, the PostgreSQL-to-PostgreSQL copy and major-version upgrade tool — priority issue handling, SLAs, and quarterly releases."
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <p class="hero-kicker">Funded upstream maintenance</p>
      <h1>pgcopydb Maintenance and Priority Support</h1>
      <p class="subtitle">PostgreSQL major-version upgrades and provider moves, with a cutover window you choose</p>
      <p>pgcopydb copies a PostgreSQL database to a target server using logical replication and parallel workers, while the source stays online. It is the practical path for a major-version upgrade or a cross-cloud move where pg_dump downtime is unacceptable &mdash; and it is what Azure Database for PostgreSQL&rsquo;s official Migration Service runs on.</p>
      <div class="hero-proof">
        <span><b>1,531</b>GitHub stars</span>
        <span><b>90k+</b>databases migrated inside Azure</span>
        <span><b>v0.18</b>Jun 2026</span>
      </div>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="https://github.com/dimitri/pgcopydb" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2 class="h-lead"><i class="fa-solid fa-copy section-icon"></i>What pgcopydb Does in an Upgrade</h2>
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
      <h2><i class="fa-solid fa-code-branch section-icon"></i>What&rsquo;s Being Worked On Right Now</h2>
      <p class="subtitle">Active maintenance areas</p>
      <p>Current work focuses on logical replication performance, broader data type coverage, improved progress reporting, and PostgreSQL version compatibility across all supported major versions.</p>
      <p>The full backlog for this project — last release, what has
      merged since, and the big features queued behind it — is on the
      <a href="/roadmap/#pgcopydb">roadmap page</a>, kept current rather than
      summarised here.</p>
    </div>
  </div>
</section>

<section class="section section_get">
  <div class="wrapper">
    <div class="content">
      <h2><i class="fa-solid fa-download section-icon"></i>Install pgcopydb</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pgcopydb is open source, actively developed, and available for Linux. Packages are available for Debian, Ubuntu, and RPM-based distributions.</p>
      <p>The <a href="https://pgcopydb.readthedocs.io/" target="_blank" rel="noopener">pgcopydb documentation</a> covers filtering, resume-on-failure, and the follow-mode cutover in detail.</p>
      <div class="buttons">
        <a href="https://github.com/dimitri/pgcopydb" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
        <a href="https://pgcopydb.readthedocs.io/" class="btn btn-secondary" target="_blank">Documentation</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_cta">
  <div class="wrapper">
    <div class="content">
      <h2>Fund pgcopydb Maintenance</h2>
      <p class="subtitle">Keep your upgrade path supported</p>
      <p>Microsoft, PlanetScale, Neon, Timescale and Meltwater all run pgcopydb in production. If your major-version upgrade or provider migration depends on it, funding its maintenance buys a defined response time on the bug you hit during the cutover window &mdash; the one moment when waiting is most expensive.</p>
      <p>Work is prioritized through one queue across all four projects,
      triaged against your tier&rsquo;s SLA, and shipped in quarterly
      releases &mdash; upstream, open source, for everyone.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="/roadmap/#pgcopydb" class="btn btn-secondary">See This Project&rsquo;s Backlog</a>
      </div>
    </div>
  </div>
</section>
