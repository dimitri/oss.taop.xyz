---
title: "pgextwlist Maintenance and Priority Support"
slug: pgextwlist
type: project-page
description: "Funded maintenance for pgextwlist, PostgreSQL extension whitelisting for non-superuser tenants — priority issue handling, SLAs, and quarterly releases."
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <p class="hero-kicker">Funded upstream maintenance</p>
      <h1>pgextwlist Maintenance and Priority Support</h1>
      <p class="subtitle">Offer CREATE EXTENSION to tenants who must never hold superuser</p>
      <p>pgextwlist intercepts <code>CREATE EXTENSION</code>, runs whitelisted extensions under superuser privileges, and drops those privileges before returning control to the caller. It is a small piece of software, and it is load-bearing everywhere it runs: without it, a managed PostgreSQL platform simply cannot offer PostGIS or pgcrypto to its customers.</p>
      <div class="hero-proof">
        <span><b>102</b>GitHub stars</span>
        <span><b>PG 10&ndash;18</b>supported</span>
        <span><b>3</b>named cloud platforms ship it</span>
      </div>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="https://github.com/dimitri/pgextwlist" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2 class="h-lead"><i class="fa-solid fa-shield-halved section-icon"></i>What pgextwlist Does for a Multi-Tenant Platform</h2>
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
      <h2><i class="fa-solid fa-code-branch section-icon"></i>What&rsquo;s Being Worked On Right Now</h2>
      <p class="subtitle">Active maintenance areas</p>
      <p>Current work focuses on PostgreSQL major-version compatibility (CI on PG 10–18), custom scripts documentation, and packaging for current Debian and RPM targets.</p>
      <p>The full backlog for this project — last release, what has
      merged since, and the big features queued behind it — is on the
      <a href="/roadmap/#pgextwlist">roadmap page</a>, kept current rather than
      summarised here.</p>
    </div>
  </div>
</section>

<section class="section section_get">
  <div class="wrapper">
    <div class="content">
      <h2><i class="fa-solid fa-download section-icon"></i>Install pgextwlist</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pgextwlist is open source and developed in public. Load it via <code>local_preload_libraries</code> and configure the whitelist with <code>extwlist.extensions</code>.</p>
      <p>The <a href="https://github.com/dimitri/pgextwlist#readme" target="_blank" rel="noopener">README</a> documents <code>extwlist.extensions</code>, the custom pre/post scripts, and packaging.</p>
      <div class="buttons">
        <a href="https://github.com/dimitri/pgextwlist" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_cta">
  <div class="wrapper">
    <div class="content">
      <h2>Fund pgextwlist Maintenance</h2>
      <p class="subtitle">Keep extension whitelisting current with every PostgreSQL major</p>
      <p>Aiven, Zalando (bundled in its Spilo image) and Microsoft Azure Database for PostgreSQL all ship pgextwlist to their own customers. A platform that offers extensions to tenants inherits this code&rsquo;s compatibility with every new PostgreSQL major; funding its maintenance is how that stays someone&rsquo;s job.</p>
      <p>Work is prioritized through one queue across all four projects,
      triaged against your tier&rsquo;s SLA, and shipped in quarterly
      releases &mdash; upstream, open source, for everyone.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="/roadmap/#pgextwlist" class="btn btn-secondary">See This Project&rsquo;s Backlog</a>
      </div>
    </div>
  </div>
</section>
