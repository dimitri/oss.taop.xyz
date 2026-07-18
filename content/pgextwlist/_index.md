---
title: "pgextwlist - PostgreSQL Extension Whitelisting"
slug: pgextwlist
type: project-page
description: "pgextwlist lets cloud providers and hosting platforms safely offer PostgreSQL extension installation to non-superuser tenants, using a whitelist and privilege-elevation model."
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <h1>pgextwlist</h1>
      <p class="subtitle">A sudo model for PostgreSQL extensions</p>
      <p>pgextwlist lets cloud providers and hosting platforms safely offer PostgreSQL extension installation to non-superuser tenants, using a whitelist and privilege-elevation model.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
        <a href="https://github.com/dimitri/pgextwlist" class="btn btn-secondary" target="_blank">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2>What pgextwlist does</h2>
      <p class="subtitle">Controlled privilege elevation for extension management</p>
      <p>pgextwlist intercepts <code>CREATE EXTENSION</code> statements and runs whitelisted ones under superuser privileges, dropping those privileges before returning control to the caller — so tenants get the extensions they need without ever holding superuser access.</p>
      <div class="value_props">
        <div class="value_prop">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <h3>Why it matters</h3>
          <p class="subtitle">Superuser is required, but cannot be granted</p>
          <ul class="use_cases_list">
            <li>PostgreSQL requires superuser to install most C-coded extensions</li>
            <li>Cloud tenants cannot be given superuser access</li>
            <li>Without a solution, extensions like PostGIS or pgcrypto are simply unavailable</li>
            <li>pgextwlist bridges the gap without compromising database security</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-server"></i>
          <h3>Typical use cases</h3>
          <p class="subtitle">Where pgextwlist fits</p>
          <ul class="use_cases_list">
            <li>Managed PostgreSQL offerings (Heroku, Aiven, Zalando Spilo, Azure Database for PostgreSQL)</li>
            <li>Kubernetes-based Postgres operators</li>
            <li>Multi-tenant SaaS platforms</li>
            <li>Private clouds where DBA and tenant roles are separate</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-bolt"></i>
          <h3>Key capabilities</h3>
          <p class="subtitle">Fine-grained control over extension lifecycle</p>
          <ul class="capabilities_list">
            <li>Per-server or per-role whitelist via <code>extwlist.extensions</code></li>
            <li>Covers CREATE, DROP, ALTER UPDATE, COMMENT ON EXTENSION</li>
            <li>Custom SQL scripts run before/after each operation</li>
            <li>Supports PostgreSQL 10 through 18</li>
            <li>Packaged for Debian, Ubuntu, and RPM distributions</li>
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
      <p>Current work focuses on PostgreSQL major-version compatibility (CI on PG 10–18), custom scripts documentation, and packaging for current Debian and RPM targets.</p>
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
      <h2>Get pgextwlist</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pgextwlist is open source and developed in public. Load it via <code>local_preload_libraries</code> and configure the whitelist with <code>extwlist.extensions</code>.</p>
      <div class="buttons">
        <a href="https://github.com/dimitri/pgextwlist" class="btn btn-secondary" target="_blank">GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_support">
  <div class="wrapper">
    <div class="content">
      <h2>Support pgextwlist</h2>
      <p class="subtitle">Keep extension whitelisting reliable</p>
      <p>If pgextwlist is part of your managed PostgreSQL stack, supporting its maintenance ensures continued PostgreSQL version compatibility, faster bug fixes, and long-term reliability for your tenants.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support This Project</a>
      </div>
    </div>
  </div>
</section>
