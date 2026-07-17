---
title: "Roadmap"
slug: roadmap
---

<section class="section section_hero_dark">
  <div class="wrapper">
    <div class="content">
      <h1>Current Work and Priorities</h1>
      <p class="subtitle">Driven by real-world usage and production issues</p>
      <div class="hero_columns">
        <p>This roadmap reflects the actual backlog across pgloader, pgcopydb, pg_auto_failover, and pgextwlist. Work is prioritized based on production impact and user support. Most items come from real-world usage &mdash; GitHub issues, production incidents, and comparison against the rest of the PostgreSQL tooling ecosystem.</p>
        <p>Most of these projects were born inside companies &mdash; an employee's or a contractor's job &mdash; with clear sponsorship behind the work. That sponsorship is gone today, even though the software is still maintained, still open source, and still relied on in production everywhere.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section_themes">
  <div class="wrapper">
    <div class="content">
      <h2>Project by Project</h2>
      <p class="subtitle">Last release, recent improvements, and what's next</p>
      <div class="project_roadmap_block" id="pg_auto_failover">
        <div class="roadmap_header">
          <div class="roadmap_header_icon"><i class="fa-solid fa-heart-pulse"></i></div>
          <div class="roadmap_header_text">
            <h3>pg_auto_failover</h3>
            <div class="release_badges">
              <span class="release_badge badge_stars"><i class="fa-solid fa-star"></i> 1,362 stars</span>
              <span class="release_badge"><i class="fa-solid fa-tag"></i> v2.2 &middot; Apr 3, 2025</span>
              <span class="release_badge badge_dev"><i class="fa-solid fa-code-branch"></i> Unreleased work &middot; Jul 2026</span>
            </div>
            <p class="known_users"><i class="fa-solid fa-building"></i> <span class="known_users_label">Known users:</span> Microsoft (Citus Data, its origin) and VMware/Broadcom Tanzu Postgres (an officially documented HA option)</p>
          </div>
        </div>
        <p>v2.2 added PostgreSQL 17 support and Citus v13 compatibility. Since then, a large PG17/18/19 and node-lifecycle body of work has merged to main, not yet tagged into a release.</p>
        <h4>Recent improvements</h4>
        <div class="improvements_grid">
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>PostgreSQL 17/18/19 compatibility work merged to main</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>New declarative <code>pg_autoctl node</code> lifecycle command for container/K8s deployments</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span><code>guard_data_loss</code> GUC and <code>--allow-data-loss</code> escape hatch for stuck multi-standby failovers</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Fixed a buffer overflow in timeline-history parsing on long-lived clusters</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Removed ~4,500 lines of unmaintained Azure integration code</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>New <code>pgaftest</code> test framework and a CI overhaul</span></div>
        </div>
        <h4>Big features on the roadmap</h4>
        <div class="value_props">
          <div class="value_prop">
            <i class="fa-solid fa-sitemap"></i>
            <h3>Multiple monitor nodes via RAFT</h3>
            <p class="subtitle">The most persistent open request since the project began</p>
            <ul class="use_cases_list">
              <li>Removes the monitor as a single point of failure</li>
              <li>RAFT-style consensus across monitor nodes, rather than a single authority</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-plug-circle-bolt"></i>
            <h3>Connection pooling as a managed node type</h3>
            <p class="subtitle">A new node kind with failover-aware reconfiguration</p>
            <ul class="use_cases_list">
              <li>Fixes the Citus <code>pg_dist_poolinfo</code> gap left stale after a failover</li>
              <li>Answers repeated requests for HAProxy/pooler integration</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-box-archive"></i>
            <h3>Disaster recovery, with archiving built in</h3>
            <p class="subtitle">HA + DR as one tool &mdash; backups stay someone else's job</p>
            <ul class="use_cases_list">
              <li>Restore a cluster from periodic base backups plus continuous WAL archiving (local cache &amp; cloud), not only from a live standby</li>
              <li>Bootstrap a whole new geo-location straight from archives, with point-in-time recovery (PITR) available across the entire cluster, not just a single node</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-earth-americas"></i>
            <h3>Cascading replication for multi-DC</h3>
            <p class="subtitle">Round-trip optimized, self-healing topologies</p>
            <ul class="use_cases_list">
              <li>Multi-datacenter deployments with round-trip-optimized replication paths</li>
              <li>Local leader maintenance if a node fails, with dynamic, automatic topology adjustments driven by a declarative setup</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-diagram-project"></i>
            <h3>Logical replication nodes</h3>
            <p class="subtitle">Mixed workloads alongside physical standbys</p>
            <ul class="use_cases_list">
              <li>First-class logical replication nodes for mixed use-cases &mdash; CDC consumers and analytics replicas alongside physical standbys</li>
              <li>Native support for <code>wal_level=logical</code>, integrated into the automated failover state machine</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-arrow-up-right-dots"></i>
            <h3>Cluster upgrades</h3>
            <p class="subtitle">Two supported paths to a new major version</p>
            <ul class="use_cases_list">
              <li>Rolling upgrades orchestrated around <code>pg_upgrade</code>, node by node</li>
              <li>Online, near-zero-downtime upgrades driven by logical replication</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="project_roadmap_block" id="pgloader">
        <div class="roadmap_header">
          <div class="roadmap_header_icon"><i class="fa-solid fa-database"></i></div>
          <div class="roadmap_header_text">
            <h3>pgloader</h3>
            <div class="release_badges">
              <span class="release_badge badge_stars"><i class="fa-solid fa-star"></i> 6,471 stars</span>
              <span class="release_badge"><i class="fa-solid fa-tag"></i> v3.6.9 &middot; stable, Oct 2022</span>
              <span class="release_badge badge_dev"><i class="fa-solid fa-flask"></i> v4 preview &middot; Jun 2026</span>
            </div>
          </div>
        </div>
        <p>pgloader is mid-rewrite: v3 (Common Lisp/SBCL) remains the stable, production release, while v4 &mdash; a from-scratch rewrite in Clojure on the JVM, distributed as a single self-contained JAR &mdash; is under active development as a drop-in replacement for v3's <code>.load</code> file syntax and CLI. The main benefit of running on the JVM: pgloader can now talk to any source database through its standard JDBC driver, already usable today, instead of needing a hand-rolled connector per source.</p>
        <h4>Recent improvements</h4>
        <div class="improvements_grid">
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>MySQL binary/UUID/inet transforms, and MSSQL Azure AD authentication (MSAL4J)</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>MSSQL <code>SEQUENCE</code> migration and multi-column foreign key fixes</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>PostgreSQL 63-character identifier collision detection (closes a decade-old issue)</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>MySQL <code>.my.cnf</code> credential lookup support</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>A sweep of longstanding CSV/fixed-width loading bugs, plus a new date-format option</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>SQLite <code>MATERIALIZE VIEWS</code> support and multi-arch v4 Docker images</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>408 issues closed and 55 PRs merged in the past two months alone, driven by the v4 rewrite push</span></div>
        </div>
        <h4>Big features on the roadmap</h4>
        <div class="value_props">
          <div class="value_prop">
            <i class="fa-solid fa-database"></i>
            <h3>Oracle as a source database</h3>
            <p class="subtitle">The most-requested source, still missing</p>
            <ul class="use_cases_list">
              <li>The single most-discussed open request on the tracker</li>
              <li>Full Oracle-to-PostgreSQL migration on par with existing MySQL/MSSQL support</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-code-merge"></i>
            <h3>ON CONFLICT DO NOTHING support</h3>
            <p class="subtitle">Upsert-style loading instead of hard failures</p>
            <ul class="use_cases_list">
              <li>Highest-reaction open issue on the tracker</li>
              <li>Avoid aborting a load on duplicate keys during incremental re-runs</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-file-code"></i>
            <h3>Emit a .sql file instead of applying it</h3>
            <p class="subtitle">A dry-run / review mode</p>
            <ul class="use_cases_list">
              <li>Let teams review or hand-apply a migration before it runs</li>
              <li>Useful for change management and compliance sign-off</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="project_roadmap_block" id="pgcopydb">
        <div class="roadmap_header">
          <div class="roadmap_header_icon"><i class="fa-solid fa-copy"></i></div>
          <div class="roadmap_header_text">
            <h3>pgcopydb</h3>
            <div class="release_badges">
              <span class="release_badge badge_stars"><i class="fa-solid fa-star"></i> 1,531 stars</span>
              <span class="release_badge"><i class="fa-solid fa-tag"></i> v0.18 &middot; Jun 27, 2026</span>
            </div>
            <p class="known_users"><i class="fa-solid fa-building"></i> <span class="known_users_label">Known users:</span> PlanetScale, Neon, Timescale (Tiger Data), Meltwater, and Microsoft &mdash; pgcopydb powers Azure Database for PostgreSQL's <a href="https://learn.microsoft.com/en-us/azure/postgresql/migrate/migration-service/overview-migration-service-postgresql" target="_blank">official, self-serve Migration Service</a>, the main driver behind its Single Server to Flexible Server migration (90k+ databases in a couple of years)</p>
          </div>
        </div>
        <p>v0.18 shipped PostgreSQL 17/18 support, made <code>pgoutput</code> the default CDC plugin, rewrote change-data-capture storage onto SQLite for crash-safe resumption, and added <code>--all-databases</code> and Citus-to-Citus migration support.</p>
        <h4>Recent improvements</h4>
        <div class="improvements_grid">
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>CDC storage rewritten onto SQLite catalogs for crash-safe resumption</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span><code>--all-databases</code> to clone an entire instance in one command</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Citus-to-Citus migration support for distributed clusters</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Regex-based filter syntax, and TimescaleDB extension support</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>AlloyDB compatibility fixes, and a <code>client_encoding</code>/SQL_ASCII COPY fix</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>LOCK TABLE failures now recover via SAVEPOINT instead of aborting the worker</span></div>
        </div>
        <h4>Big features on the roadmap</h4>
        <div class="value_props">
          <div class="value_prop">
            <i class="fa-solid fa-tower-broadcast"></i>
            <h3>Publication/subscription follow mode</h3>
            <p class="subtitle">The model AWS DMS, Google Cloud DMS, and pglogical build on</p>
            <ul class="use_cases_list">
              <li>Lets tables be added mid-migration without a fresh snapshot</li>
              <li>Aligns pgcopydb's CDC engine with the pub/sub model used across the ecosystem</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-code-compare"></i>
            <h3>Automatic DDL/schema-drift sync</h3>
            <p class="subtitle">Keep up with the source during <code>--follow</code></p>
            <ul class="use_cases_list">
              <li>Propagate new tables/schemas created on the source after initial sync</li>
              <li>The most-cited gap versus native logical replication workflows</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-filter"></i>
            <h3>Finer-grained filtering</h3>
            <p class="subtitle">Roles, foreign keys, and casts</p>
            <ul class="use_cases_list">
              <li>Extends the regex filter system shipped in v0.18 to more object types</li>
              <li>Avoids clobbering operational roles and custom casts already on the target</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-flag-checkered"></i>
            <h3>Built-in cutover orchestration</h3>
            <p class="subtitle">A turnkey <code>pgcopydb switchover</code></p>
            <ul class="use_cases_list">
              <li>Check replication lag and confirm safe-to-flip automatically</li>
              <li>The last-mile step tools like pg_easy_replicate already offer</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="project_roadmap_block" id="pgextwlist">
        <div class="roadmap_header">
          <div class="roadmap_header_icon"><i class="fa-solid fa-list-check"></i></div>
          <div class="roadmap_header_text">
            <h3>pgextwlist</h3>
            <div class="release_badges">
              <span class="release_badge badge_stars"><i class="fa-solid fa-star"></i> 102 stars</span>
              <span class="release_badge"><i class="fa-solid fa-tag"></i> v1.20 &middot; Jul 8, 2026</span>
            </div>
            <p class="known_users"><i class="fa-solid fa-building"></i> <span class="known_users_label">Known users:</span> Aiven, Zalando (bundled in its Spilo Postgres image), and Microsoft Azure Database for PostgreSQL</p>
          </div>
        </div>
        <p>v1.20 fixed a SQL-injection vector in extension schema/owner substitution (CVE-2023-39417) and added <code>extwlist.restrict_to_database_owner</code> for finer-grained control over who can install whitelisted extensions.</p>
        <h4>Recent improvements</h4>
        <div class="improvements_grid">
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>PostgreSQL 18 compatibility, with PG 19/20 already in the CI test matrix</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Extension drop-hook and <code>COMMENT ON EXTENSION</code> support</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Transaction-validity checking before superuser operations</span></div>
          <div class="improvement_item"><i class="fa-solid fa-circle-check"></i><span>Packaging repository moved to Debian Salsa</span></div>
        </div>
        <h4>Big features on the roadmap</h4>
        <div class="value_props">
          <div class="value_prop">
            <i class="fa-solid fa-cloud-arrow-down"></i>
            <h3>On-demand extension installation</h3>
            <p class="subtitle">Reviving the pginstall model</p>
            <ul class="use_cases_list">
              <li>Fetch and install whitelisted extensions from a build-farm-backed registry at <code>CREATE EXTENSION</code> time, instead of requiring them pre-installed on disk</li>
              <li>Modernizes <a href="https://github.com/dimitri/pginstall" target="_blank">pginstall</a>, Dimitri's earlier, more ambitious follow-on to pgextwlist &mdash; dormant since 2016 but cited as prior art in PGXN v2's current binary-packaging redesign</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-boxes-stacked"></i>
            <h3>Private, mirrored extension repositories</h3>
            <p class="subtitle">For cloud providers and enterprises</p>
            <ul class="use_cases_list">
              <li>Whitelist internal, non-public extensions alongside upstream ones</li>
              <li>Drawn directly from pginstall's own design docs for mirroring and merging upstream repositories</li>
            </ul>
          </div>
          <div class="value_prop">
            <i class="fa-solid fa-user-lock"></i>
            <h3>Finer-grained per-role/per-database controls</h3>
            <p class="subtitle">Building on v1.20's ownership check</p>
            <ul class="use_cases_list">
              <li>Extends <code>extwlist.restrict_to_database_owner</code> with more granular role- and database-scoped policies</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section_meaning">
  <div class="wrapper">
    <div class="content">
      <h2>What this means</h2>
      <p>This is not a speculative roadmap. It is a reflection of actual production needs across teams using these tools today. Supporting the projects directly influences what gets fixed, improved, and released next.</p>
    </div>
  </div>
</section>

<section class="section section_prioritized">
  <div class="wrapper">
    <div class="content">
      <h2>How work is prioritized</h2>
      <ul class="priority_list">
        <li>Production blockers and data-loss risks come first</li>
        <li>Paid support tiers move issues forward in the queue</li>
        <li>Work is grouped and shipped in quarterly releases</li>
        <li>Cross-project improvements are prioritized when they unlock multiple use cases</li>
      </ul>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">See support options</a>
      </div>
    </div>
  </div>
</section>

<section class="section section_cta">
  <div class="wrapper">
    <div class="content">
      <h2>Influence the roadmap</h2>
      <p class="subtitle">Fund the work that matters to you</p>
      <div class="buttons">
        <a href="/#pricing" class="btn btn-primary">Support These Projects</a>
        <a href="/projects/" class="btn btn-secondary">View Projects</a>
      </div>
    </div>
  </div>
</section>
