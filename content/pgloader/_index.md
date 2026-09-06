---
title: "pgloader Maintenance and Priority Support"
slug: pgloader
type: project-page
description: "Funded maintenance for pgloader, the MySQL, SQLite and MS SQL Server to PostgreSQL migration tool — priority issue handling, SLAs, and quarterly releases."
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <p class="hero-kicker">Funded upstream maintenance</p>
      <h1>pgloader Maintenance and Priority Support</h1>
      <p class="subtitle">Migrating MySQL, SQLite or MS SQL Server to PostgreSQL, on a schedule you can commit to</p>
      <p>pgloader connects to the source database, converts the schema to PostgreSQL conventions, and loads the data in parallel from a single command. It has been maintained since 2005 and is the tool named in nearly every MySQL-to-PostgreSQL migration guide written since. This page is about funding that maintenance &mdash; the tool itself is free, and stays that way.</p>
      <div class="hero-proof">
        <span><b>6,471</b>GitHub stars</span>
        <span><b>2005</b>maintained since</span>
        <span><b>4</b>live source databases</span>
      </div>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="https://github.com/dimitri/pgloader" class="btn btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_solution">
  <div class="wrapper">
    <div class="content">
      <h2 class="h-lead"><i class="fa-solid fa-truck-fast section-icon"></i>What pgloader Does in a Migration</h2>
      <p class="subtitle">Automated schema conversion and high-performance loading</p>
      <p>pgloader connects directly to the source database, converts the schema to PostgreSQL conventions, and loads all data in a single command. It handles real-world edge cases — encoding issues, type mismatches, constraint ordering — so you don't have to.</p>
      <div class="value_props">
        <div class="value_prop">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <h3>Why it matters</h3>
          <p class="subtitle">Manual migrations are error-prone and slow</p>
          <ul class="use_cases_list">
            <li>Schema differences between databases require careful translation</li>
            <li>Data type mismatches cause silent corruption if not handled correctly</li>
            <li>Large datasets need parallel loading to be practical</li>
            <li>pgloader automates the tedious parts and reports exactly what it changed</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-database"></i>
          <h3>Supported sources</h3>
          <p class="subtitle">Migrate from wherever your data lives</p>
          <ul class="use_cases_list">
            <li>MySQL and MariaDB</li>
            <li>SQLite</li>
            <li>MS SQL Server</li>
            <li>CSV, Fixed-width, and dBase files</li>
            <li>PostgreSQL (for restructuring or copying)</li>
          </ul>
        </div>
        <div class="value_prop">
          <i class="fa-solid fa-bolt"></i>
          <h3>Key capabilities</h3>
          <p class="subtitle">Production-grade data loading</p>
          <ul class="capabilities_list">
            <li>Automatic schema and type conversion</li>
            <li>Parallel loading with concurrent workers</li>
            <li>Error reporting with per-row rejection logs</li>
            <li>Scriptable with a dedicated command language</li>
            <li>Docker image available</li>
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
      <p>Current work focuses on compatibility with recent MySQL and PostgreSQL versions, edge cases in schema conversion, and packaging for current distributions.</p>
      <p>The full backlog for this project — last release, what has
      merged since, and the big features queued behind it — is on the
      <a href="/roadmap/#pgloader">roadmap page</a>, kept current rather than
      summarised here.</p>
    </div>
  </div>
</section>

<section class="section section_get">
  <div class="wrapper">
    <div class="content">
      <h2><i class="fa-solid fa-download section-icon"></i>Install pgloader</h2>
      <p class="subtitle">Open source and available now</p>
      <p>pgloader is open source and available as a binary, Debian/Ubuntu package, or Docker image. A single command is often all it takes to start a migration.</p>
      <p><a href="https://pgloader.io" target="_blank" rel="noopener">pgloader.io</a> carries the full documentation, the source list, and the Continuous Migration method the tool was built for.</p>
      <div class="buttons">
        <a href="https://github.com/dimitri/pgloader" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
        <a href="https://pgloader.io" class="btn btn-secondary" target="_blank">Documentation</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_cta">
  <div class="wrapper">
    <div class="content">
      <h2>Fund pgloader Maintenance</h2>
      <p class="subtitle">Keep MySQL and MS SQL Server migrations working</p>
      <p>If a migration on your roadmap depends on pgloader, funding its maintenance is what turns "someone will get to it" into a date. Sponsored work here has a track record: MS SQL Server support exists because Redpill Linpro paid for it, and it shipped free for everyone.</p>
      <p>Work is prioritized through one queue across all four projects,
      triaged against your tier&rsquo;s SLA, and shipped in quarterly
      releases &mdash; upstream, open source, for everyone.</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See Pricing &amp; Tiers</a>
        <a href="/roadmap/#pgloader" class="btn btn-secondary">See This Project&rsquo;s Backlog</a>
      </div>
    </div>
  </div>
</section>
