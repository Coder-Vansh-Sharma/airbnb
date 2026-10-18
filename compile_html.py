#!/usr/bin/env python3
import json

# Load the enhanced massive prompt library (342+ high-detail prompts with Hinglish)
with open('prompts_data_massive.json', 'r', encoding='utf-8') as f:
    prompts_data = json.load(f)

print(f"Loaded {len(prompts_data)} high-detail prompts.")

with open('app_styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('app_script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

prompts_json_escaped = json.dumps(prompts_data, ensure_ascii=False).replace('</script>', '<\\/script>')

# HTML Body Markup
HTML_BODY = f"""
<div id="hm-app" class="hm-app">
  <div class="hm-container">
    
    <!-- TOP BAR -->
    <header class="hm-topbar">
      <div class="hm-brand-group">
        <div class="hm-logo-badge">H</div>
        <div class="hm-brand-titles">
          <h1>HostMastery <span style="font-size:12px;color:var(--hm-coral);font-weight:700">★ PRO</span></h1>
          <p>The All-in-One Airbnb Host Kit</p>
        </div>
      </div>
      <div class="hm-top-actions">
        <!-- GLOBAL LANGUAGE MODE TOGGLE -->
        <div class="hm-lang-switcher" title="Toggle prompt language mode">
          <button class="hm-lang-opt hm-active" data-lang="hinglish">🇮🇳 Hinglish Mode</button>
          <button class="hm-lang-opt" data-lang="en">🇬🇧 English</button>
        </div>

        <button class="hm-btn hm-btn-soft" id="btn-open-profile">🏠 My Property</button>
        <button class="hm-btn hm-btn-outline" data-go="prompts" id="btn-top-favs">⭐ Saved (<span id="top-fav-count">0</span>)</button>
        <button class="hm-btn hm-btn-coral" id="btn-open-wizard">⚡ 10,000+ Wizard</button>
        <button class="hm-btn hm-btn-primary" id="btn-open-export">📦 Export Kit</button>
      </div>
    </header>

    <!-- HERO DASHBOARD -->
    <section class="hm-hero">
      <div class="hm-hero-pill"><span class="hm-hero-pill-dot"></span> The Complete Growth Suite for Indian Stays</div>
      <h2>Make your stay easier to <span>discover, book & love.</span></h2>
      <p>340+ curated high-detail master prompts, 10,000+ combinations AI matrix engine, 1-click Hinglish guest messages, and printable in-room Welcome Studio — crafted specifically for Indian Airbnb hosts, villas & homestays.</p>
      
      <div class="hm-hero-search">
        <span class="hm-hero-search-icon">🔍</span>
        <input type="text" id="hm-hero-search-input" placeholder="Search anything: 'reels script', 'wifi card', 'diwali campaign', 'power cut whatsapp', 'pricing formula'…">
        <button class="hm-btn hm-btn-primary hm-btn-sm" onclick="document.getElementById('hm-hero-search-input').focus()">Search All</button>
      </div>

      <div class="hm-hero-stats">
        <div class="hm-hero-stat-card">
          <div class="hm-hero-stat-num" id="hm-total-prompts-count">{len(prompts_data)}+</div>
          <div class="hm-hero-stat-label">Ready Master Prompts</div>
        </div>
        <div class="hm-hero-stat-card">
          <div class="hm-hero-stat-num">10,000+</div>
          <div class="hm-hero-stat-label">AI Matrix Combinations</div>
        </div>
        <div class="hm-hero-stat-card">
          <div class="hm-hero-stat-num">Dual Mode</div>
          <div class="hm-hero-stat-label">Hinglish & English</div>
        </div>
        <div class="hm-hero-stat-card">
          <div class="hm-hero-stat-num">5 Ready</div>
          <div class="hm-hero-stat-label">Printable Studio Sheets</div>
        </div>
      </div>
    </section>

    <!-- QUICK JUMP HUB CARDS -->
    <div class="hm-quick-hubs">
      <div class="hm-hub-card" data-go="prompts">
        <div class="hm-hub-icon">✦</div>
        <div class="hm-hub-info">
          <b>Prompt Library</b>
          <span>{len(prompts_data)}+ Prompts & Matrix</span>
        </div>
      </div>
      <div class="hm-hub-card" data-go="growth">
        <div class="hm-hub-icon">🚀</div>
        <div class="hm-hub-info">
          <b>Listing Growth</b>
          <span>Audit & Photos</span>
        </div>
      </div>
      <div class="hm-hub-card" data-go="social">
        <div class="hm-hub-icon">📱</div>
        <div class="hm-hub-info">
          <b>Social Studio</b>
          <span>Reels & Hooks</span>
        </div>
      </div>
      <div class="hm-hub-card" data-go="guest">
        <div class="hm-hub-icon">🤝</div>
        <div class="hm-hub-info">
          <b>Guest & Welcome</b>
          <span>Messages & Print</span>
        </div>
      </div>
      <div class="hm-hub-card" data-go="resources">
        <div class="hm-hub-icon">📊</div>
        <div class="hm-hub-info">
          <b>Host Resources</b>
          <span>Pricing Calc & Plan</span>
        </div>
      </div>
      <div class="hm-hub-card" data-go="academy">
        <div class="hm-hub-icon">🎓</div>
        <div class="hm-hub-info">
          <b>Learn & Academy</b>
          <span>Beginner Guides</span>
        </div>
      </div>
    </div>

    <!-- 6 PRIMARY SECTIONS TAB NAVIGATION -->
    <nav class="hm-main-nav" role="tablist" aria-label="HostMastery Sections">
      <button class="hm-tab-btn" role="tab" aria-selected="true" data-tab="prompts">✦ AI Prompt Library & Matrix</button>
      <button class="hm-tab-btn" role="tab" aria-selected="false" data-tab="growth">🚀 Listing Growth</button>
      <button class="hm-tab-btn" role="tab" aria-selected="false" data-tab="social">📱 Social Media Studio</button>
      <button class="hm-tab-btn" role="tab" aria-selected="false" data-tab="guest">🤝 Guest Experience & Welcome</button>
      <button class="hm-tab-btn" role="tab" aria-selected="false" data-tab="resources">📊 Host Resources & Calc</button>
      <button class="hm-tab-btn" role="tab" aria-selected="false" data-tab="academy">🎓 Learn & Improve</button>
    </nav>

    <!-- ==================== SECTION 1: AI PROMPT LIBRARY ==================== -->
    <section class="hm-view hm-active" data-view="prompts">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Copy · Personalize · Generate</div>
          <h2>AI Prompt Library & 10,000+ Combinator Matrix</h2>
          <p>Search over {len(prompts_data)}+ curated high-detail master prompts, or use the infinity matrix below to generate bespoke prompts for any Indian location and stay type in Hinglish or English!</p>
        </div>
        <span class="hm-badge-india">🇮🇳 100% Hinglish & English Supported</span>
      </div>

      <!-- 10,000+ COMBINATIONS AI PROMPT MATRIX ENGINE -->
      <div class="hm-matrix-box">
        <div class="hm-matrix-title-row">
          <div>
            <h3 style="margin:0 0 4px;font-size:16px;color:var(--hm-primary);font-weight:850">⚡ The 10,000+ Combinations Prompt Matrix Engine</h3>
            <p style="margin:0;font-size:12px;color:var(--hm-muted)">Select your parameters to instantly generate a custom, multi-paragraph master prompt ready to copy into ChatGPT or Gemini.</p>
          </div>
          <span style="background:var(--hm-accent);color:var(--hm-primary);font-size:11px;font-weight:800;padding:4px 10px;border-radius:99px">26,000+ Unique Combinations</span>
        </div>

        <div class="hm-matrix-grid">
          <div class="hm-matrix-field">
            <label>1. Indian Destination</label>
            <select id="mat-dest">
              <option value="Manali, Himachal Pradesh">Manali & Kullu Valley (HP)</option>
              <option value="Goa (North & South)">Goa (Beaches & Heritage)</option>
              <option value="Jaipur / Udaipur, Rajasthan">Jaipur / Udaipur (Rajasthan)</option>
              <option value="Coorg / Chikmagalur, Karnataka">Coorg & Chikmagalur (Karnataka)</option>
              <option value="Lonavala / Alibaug, Maharashtra">Lonavala & Alibaug (Maharashtra)</option>
              <option value="Rishikesh, Uttarakhand">Rishikesh & Ganga Valley (UK)</option>
              <option value="Munnar / Wayanad, Kerala">Munnar & Wayanad (Kerala)</option>
              <option value="Pondicherry (White Town)">Pondicherry & Auroville</option>
              <option value="Gokarna, Karnataka">Gokarna Coastal Stays</option>
              <option value="Delhi NCR / Gurugram">Delhi NCR & Gurugram</option>
              <option value="Kashmir (Srinagar / Pahalgam)">Kashmir (Srinagar / Pahalgam)</option>
              <option value="Jim Corbett / Ranthambore">Jim Corbett & Forest Safaris</option>
              <option value="Shimla / Mashobra, HP">Shimla & Mashobra (HP)</option>
              <option value="Ooty / Kodaikanal, Tamil Nadu">Ooty & Kodaikanal (TN)</option>
              <option value="Varanasi, Uttar Pradesh">Varanasi Ghats & Heritage</option>
            </select>
          </div>

          <div class="hm-matrix-field">
            <label>2. Property Type</label>
            <select id="mat-type">
              <option value="Boutique Mountain Homestay / Pine Cabin">Boutique Mountain Homestay</option>
              <option value="Luxury Private Villa with Pool">Luxury Private Pool Villa</option>
              <option value="Heritage Haveli / Royal Courtyard Suite">Heritage Haveli / Traditional Home</option>
              <option value="Coffee Estate Plantation Homestay">Coffee Plantation Estate</option>
              <option value="Scenic Farmhouse & Lawn Retreat">Scenic Farmhouse with Lawn</option>
              <option value="Beachfront Cottage / Portuguese Villa">Beach Cottage / Coastal Villa</option>
              <option value="City Workation Flat / Modern Studio">City Workation Studio Flat</option>
              <option value="Riverside Wellness & Yoga Sanctuary">Riverside Wellness Sanctuary</option>
              <option value="Wildlife Forest Lodge / Glamping Camp">Wildlife Forest Lodge / Camp</option>
            </select>
          </div>

          <div class="hm-matrix-field">
            <label>3. Target Traveler</label>
            <select id="mat-aud">
              <option value="Romantic Couples & Honeymooners">Romantic Couples & Honeymooners</option>
              <option value="Families with Kids & Elders">Families with Kids & Elders</option>
              <option value="Remote Workers / Workationers">Remote Workers / Workationers</option>
              <option value="Weekend Friends / Road-trippers">Weekend Friends & Road-trippers</option>
              <option value="Solo Travelers & Slow Explorers">Solo Travelers & Slow Explorers</option>
              <option value="Pet Parents / Dog Friendly Travelers">Pet Parents (Dog Friendly)</option>
              <option value="Corporate Offsites / Small Teams">Corporate Offsite / Small Teams</option>
            </select>
          </div>

          <div class="hm-matrix-field">
            <label>4. Content & Marketing Goal</label>
            <select id="mat-goal">
              <option value="Viral 15-Second Aesthetic Reel Script">Viral 15s Aesthetic Reel Script</option>
              <option value="30-Second Room-by-Room Walkthrough Script">30s Room-by-Room Walkthrough</option>
              <option value="20 High-CTR Airbnb Listing Titles">20 High-CTR Listing Titles</option>
              <option value="Full High-Converting Listing Description">Full Listing Description</option>
              <option value="7-Slide Local Insider Guide Carousel">7-Slide Local Guide Carousel</option>
              <option value="Pre-Booking Guest FAQs Section">Pre-Booking Guest FAQs Section</option>
              <option value="Warm Yet Enforceable House Rules">Warm Yet Enforceable House Rules</option>
              <option value="Weekend vs Weekday Pricing Formula">Weekend vs Weekday Pricing Formula</option>
              <option value="Festival Long-Weekend Campaign (Diwali/New Year)">Festival Campaign (Diwali/New Year)</option>
              <option value="Room-by-Room Smartphone Photo Staging Plan">Smartphone Photo Staging Plan</option>
              <option value="Sudden Power Cut / Inverter Message">Sudden Power Cut / Inverter Message</option>
              <option value="Post-Stay 5-Star Review Invitation">Post-Stay 5-Star Review Request</option>
            </select>
          </div>

          <div class="hm-matrix-field">
            <label>5. Language Tone</label>
            <select id="mat-lang">
              <option value="hinglish">Conversational Hinglish (Recommended) 🇮🇳</option>
              <option value="en">Professional Indian English 🇬🇧</option>
            </select>
          </div>
        </div>

        <div class="hm-matrix-actions">
          <button class="hm-btn hm-btn-primary" id="btn-matrix-generate">⚡ Generate Bespoke Prompt</button>
          <button class="hm-btn hm-btn-soft" id="btn-matrix-random">🎲 Random Lucky Combination</button>
        </div>

        <div id="hm-matrix-result-box" class="hm-matrix-result">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <b style="font-size:13px;color:var(--hm-primary)">Generated Custom Master Prompt:</b>
            <button class="hm-btn hm-btn-primary hm-btn-sm" id="btn-matrix-copy">📋 Copy Master Prompt</button>
          </div>
          <pre id="hm-matrix-pre"></pre>
        </div>
      </div>

      <!-- MAIN PROMPT CATALOG -->
      <div class="hm-lib-grid">
        <!-- Sidebar Categories -->
        <aside class="hm-lib-sidebar">
          <div class="hm-sidebar-heading">Filter by Hub</div>
          <div id="hm-categories-list" class="hm-category-menu"></div>
          
          <div style="border-top:1px solid var(--hm-line);margin-top:14px;padding-top:14px">
            <div style="font-size:11px;font-weight:750;color:var(--hm-primary);margin-bottom:6px">💡 Hinglish Pro Tip</div>
            <p style="font-size:11px;color:var(--hm-muted);line-height:1.5;margin:0 0 10px">Prompts me real property details use karo. Har card par <b>🇮🇳 Hinglish</b> button press karke seedha Hindi-English hybrid prompt copy karein.</p>
            <button class="hm-btn hm-btn-outline hm-btn-sm" style="width:100%" data-go="academy">Open Prompt Academy ↗</button>
          </div>
        </aside>

        <!-- Main Prompts Stream -->
        <div class="hm-lib-main">
          <div class="hm-lib-toolbar">
            <div class="hm-search-box">
              <span class="hm-search-icon-lib">⌕</span>
              <input type="search" id="hm-lib-search" placeholder="Search prompts: reels, title, dining, pricing, wifi, manali, goa...">
            </div>

            <label class="hm-toggle-personalize" title="Automatically replaces [property type], [location], [amenities] with your real details">
              <input type="checkbox" id="hm-toggle-personalize-chk">
              <span>⚡ Auto-Personalize</span>
            </label>

            <button class="hm-btn hm-btn-primary hm-btn-sm" id="hm-copy-visible-pack">📋 Copy Visible Pack</button>
          </div>

          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;font-size:12px;color:var(--hm-muted);flex-wrap:wrap;gap:8px">
            <span id="hm-result-count">Showing prompts</span>
            <span>Switch card language anytime: <b>🇮🇳 Hinglish | 🇬🇧 English</b></span>
          </div>

          <!-- PROMPT CARDS GRID -->
          <div id="hm-prompt-grid" class="hm-prompt-cards-grid" aria-live="polite"></div>

          <!-- LOAD MORE BUTTON -->
          <div id="hm-load-more-container" class="hm-load-more-row" style="display:none">
            <button class="hm-btn hm-btn-soft" id="btn-load-more" style="padding:10px 24px;font-size:13px">⚡ Load More Prompts</button>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SECTION 2: LISTING GROWTH ==================== -->
    <section class="hm-view" data-view="growth">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Audit · Optimize · Rank Higher</div>
          <h2>Listing Growth Hub</h2>
          <p>Score your Airbnb listing out of 100 with our interactive audit, verify your photo sequence, and eliminate common mistakes that turn guests away.</p>
        </div>
      </div>

      <div class="hm-growth-grid">
        <!-- Interactive 10-Point Audit Tool -->
        <div class="hm-audit-card">
          <div class="hm-score-banner">
            <div class="hm-score-circle">
              <div class="hm-score-digit" id="hm-audit-score-digit">85</div>
              <div>
                <b style="font-size:15px;display:block">Listing Health Score</b>
                <span id="hm-audit-badge" style="display:inline-block;padding:2px 8px;border-radius:99px;font-size:11px;font-weight:800;margin-top:3px">⭐ Superhost Ready Listing</span>
              </div>
            </div>
            <button class="hm-btn hm-btn-soft hm-btn-sm" onclick="window.print()">⎙ Print Audit</button>
          </div>

          <h3 style="font-size:16px;font-weight:800;margin:0 0 8px;color:var(--hm-primary)">Interactive 10-Point Listing Assessment</h3>
          <p style="font-size:12px;color:var(--hm-muted);margin:0 0 16px">Answer honestly based on your live Airbnb listing. Your customized improvement checklist updates in real time.</p>

          <div id="hm-audit-questions-list"></div>
        </div>

        <!-- Right Side: Tailored Action Items + 5-Photo Strategy -->
        <div>
          <div class="hm-checklist-box">
            <h3>⚡ Tailored Action Checklist</h3>
            <p style="font-size:12px;color:var(--hm-muted);margin:0 0 14px">Based on your audit answers, here are the highest-impact improvements to boost conversion:</p>
            <div id="hm-audit-action-items"></div>
          </div>

          <div class="hm-checklist-box">
            <h3>📸 The Golden 5-Photo Hero Order</h3>
            <p style="font-size:12px;color:var(--hm-muted);margin:0 0 12px">On mobile, 80% of guests decide whether to tap based on the first 5 photos:</p>
            <div style="font-size:12px;display:flex;flex-direction:column;gap:8px">
              <div style="background:#f7faf5;padding:10px 12px;border-radius:8px;border-left:3px solid var(--hm-primary)">
                <b>Photo 1 (Hero Cover):</b> Bright living room angle with view or stunning exterior shot. Must have crisp daylight and no wide-angle blur.
              </div>
              <div style="background:#f7faf5;padding:10px 12px;border-radius:8px;border-left:3px solid var(--hm-primary)">
                <b>Photo 2 (Master Bedroom):</b> Freshly pressed white linens, clean pillows, bedside lamps, showing sleeping comfort clearly.
              </div>
              <div style="background:#f7faf5;padding:10px 12px;border-radius:8px;border-left:3px solid var(--hm-primary)">
                <b>Photo 3 (The Standout Angle):</b> Private balcony with chai setup, mountain/pool view, or cozy reading nook.
              </div>
              <div style="background:#f7faf5;padding:10px 12px;border-radius:8px;border-left:3px solid var(--hm-primary)">
                <b>Photo 4 (Spotless Bathroom):</b> Demonstrates hygiene, geyser/hot water, dry floor, fresh towels and toiletries.
              </div>
              <div style="background:#f7faf5;padding:10px 12px;border-radius:8px;border-left:3px solid var(--hm-primary)">
                <b>Photo 5 (Workation / Kitchen):</b> Shows dedicated desk with Wi-Fi speed test or fully equipped kitchen for self-cooking.
              </div>
            </div>
          </div>

          <div class="hm-checklist-box">
            <h3>⚠️ Top 3 Mistakes of Indian Homestays</h3>
            <ul style="padding-left:18px;margin:8px 0;font-size:12px;color:#3b4d45;line-height:1.6">
              <li><b>Overpromising Wi-Fi:</b> Calling a 10 Mbps connection "Ultra High Speed 200 Mbps" leads to immediate 1-star reviews from remote workers.</li>
              <li><b>Hiding Constraints:</b> Not mentioning that the property is on the 3rd floor without a lift. Always state stair counts upfront.</li>
              <li><b>Ambiguous Visitor Rules:</b> Clearly disclose whether unregistered local friends are allowed in the room or only in the common lounge.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SECTION 3: SOCIAL MEDIA STUDIO ==================== -->
    <section class="hm-view" data-view="social">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Reels · Captions · Viral Hooks · Festivals</div>
          <h2>Social Media Studio</h2>
          <p>Everything you need to turn phone videos into high-engagement Reels, plan carousels, and run campaigns around Indian long weekends and festivals.</p>
        </div>
      </div>

      <!-- Viral Hooks Generator -->
      <div class="hm-checklist-box" style="margin-bottom:24px">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:12px">
          <div>
            <h3 style="margin:0 0 4px">⚡ 25+ Viral Hooks Generator for Indian Homestays</h3>
            <p style="font-size:12px;color:var(--hm-muted);margin:0">High-converting 2-second opening lines for Instagram Reels & Shorts.</p>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap">
            <button class="hm-btn hm-btn-soft hm-btn-sm" onclick="window.renderHooks('All')">All</button>
            <button class="hm-btn hm-btn-outline hm-btn-sm" onclick="window.renderHooks('Aesthetic')">Aesthetic</button>
            <button class="hm-btn hm-btn-outline hm-btn-sm" onclick="window.renderHooks('Curiosity')">Curiosity</button>
            <button class="hm-btn hm-btn-outline hm-btn-sm" onclick="window.renderHooks('Value')">Value</button>
            <button class="hm-btn hm-btn-outline hm-btn-sm" onclick="window.renderHooks('Hospitality')">Hospitality</button>
            <button class="hm-btn hm-btn-outline hm-btn-sm" onclick="window.renderHooks('Weekend')">Weekend</button>
          </div>
        </div>
        <div id="hm-hooks-list"></div>
      </div>

      <!-- Reels Video Vault & Festival Calendar -->
      <div class="hm-social-grid">
        <!-- Script 1 -->
        <article class="hm-social-card">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span class="hm-pill-cat">🎬 30-Sec Reel Script</span>
            <span style="font-size:11px;font-weight:750;color:var(--hm-muted)">Property Tour</span>
          </div>
          <h3 style="font-size:15px;margin:0;color:var(--hm-primary)">The Scenic 30-Second Tour</h3>
          <div style="font-size:11.5px;line-height:1.55;color:#3b4d45;background:#f8faf6;padding:12px;border-radius:10px">
            <b>[0:00 - 0:03] Hook:</b> Push open balcony door with steam rising from chai cup. Text: <i>"Finding peace in [City] hits different here."</i><br><br>
            <b>[0:03 - 0:10] Bedroom:</b> Smooth pan of the plush white bed and morning sunlight.<br><br>
            <b>[0:10 - 0:18] Standout Amenity:</b> Work desk with mountains in background or cozy garden bonfire.<br><br>
            <b>[0:18 - 0:25] Bathroom & Hygiene:</b> Quick 2-second flash showing spotless hygiene & warm lighting.<br><br>
            <b>[0:25 - 0:30] CTA:</b> Sunset shot with on-screen text: <i>"Link in bio to check available dates on Airbnb!"</i>
          </div>
          <button class="hm-btn hm-btn-primary hm-btn-sm" onclick="window.copyScript('30sec')">📋 Copy Script & Audio Notes</button>
        </article>

        <!-- Script 2 -->
        <article class="hm-social-card">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span class="hm-pill-cat">🎬 No-Face Reel Script</span>
            <span style="font-size:11px;font-weight:750;color:var(--hm-muted)">Aesthetic / POV</span>
          </div>
          <h3 style="font-size:15px;margin:0;color:var(--hm-primary)">The Peaceful POV Workation</h3>
          <div style="font-size:11.5px;line-height:1.55;color:#3b4d45;background:#f8faf6;padding:12px;border-radius:10px">
            <b>Audio:</b> Acoustic guitar or lo-fi ambient rain.<br>
            <b>Visual 1:</b> Hands setting laptop on wooden desk overlooking the greenery.<br>
            <b>Visual 2:</b> Opening browser with 100 Mbps Wi-Fi speed test shown on screen.<br>
            <b>Visual 3:</b> Pouring hot coffee or tea into an earthenware mug.<br>
            <b>On-Screen Text:</b> <i>"Taking Zoom meetings with this view is my new non-negotiable."</i><br>
            <b>Caption:</b> <i>"Tag your coworker who needs a change of scenery. 📍 [Property Name], [City]."</i>
          </div>
          <button class="hm-btn hm-btn-primary hm-btn-sm" onclick="window.copyScript('noface')">📋 Copy Script & Audio Notes</button>
        </article>

        <!-- Indian Festival Calendar -->
        <article class="hm-social-card" style="grid-column:1/-1">
          <h3 style="font-size:16px;margin:0 0 6px;color:var(--hm-primary)">🇮🇳 Indian Festive & Long-Weekend Marketing Calendar</h3>
          <p style="font-size:12px;color:var(--hm-muted);margin:0 0 14px">Plan your promotional posts 3–4 weeks before peak booking windows:</p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:12px">
            <div style="background:#fdfaf3;border:1px solid #fae8cc;border-radius:10px;padding:12px">
              <b style="color:#b45309;font-size:13px">Q1: Republic Day & Holi Getaways</b>
              <p style="font-size:11.5px;color:#78350f;margin:4px 0 0">Promote group stays & organic Holi celebrations. Start posting in mid-January and late February.</p>
            </div>
            <div style="background:#f3fcf6;border:1px solid #ccefd8;border-radius:10px;padding:12px">
              <b style="color:#15803d;font-size:13px">Q2: Summer Vacation Peak</b>
              <p style="font-size:11.5px;color:#14532d;margin:4px 0 0">Family vacations escaping the plains heat. Highlight cooling balconies, mountain treks, or private plunge pools. Post in April.</p>
            </div>
            <div style="background:#f4f9fd;border:1px solid #cee5f9;border-radius:10px;padding:12px">
              <b style="color:#1d4ed8;font-size:13px">Q3: Monsoon Escapes & Aug 15</b>
              <p style="font-size:11.5px;color:#1e3a8a;margin:4px 0 0">Lush green landscapes, hot pakoras, misty views. Target couples and road-trippers 2 weeks prior.</p>
            </div>
            <div style="background:#fdf4f8;border:1px solid #fad2e6;border-radius:10px;padding:12px">
              <b style="color:#be185d;font-size:13px">Q4: Diwali, Christmas & New Year</b>
              <p style="font-size:11.5px;color:#831843;margin:4px 0 0">Peak ADR (nightly rate) of the year. Open calendar 60 days ahead with minimum 3-night stay restrictions.</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <!-- ==================== SECTION 4: GUEST EXPERIENCE & WELCOME ==================== -->
    <section class="hm-view" data-view="guest">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Automate & Impress</div>
          <h2>Guest Experience & Welcome Studio</h2>
          <p>Send professional 1-click messages in Hinglish, English, or Hindi, and design print-ready in-room welcome sheets, Wi-Fi cards, and house rules.</p>
        </div>
      </div>

      <!-- SUBTABS FOR GUEST HUB -->
      <div class="hm-guest-tabs">
        <button class="hm-btn hm-btn-soft" id="subtab-btn-msgs" onclick="window.switchGuestSubtab('msgs')">💬 Guest Communication Messages (12 Templates)</button>
        <button class="hm-btn hm-btn-outline" id="subtab-btn-studio" onclick="window.switchGuestSubtab('studio')">▤ Printable Welcome Studio (5 Layouts)</button>
      </div>

      <!-- SUBTAB 1: GUEST MESSAGES -->
      <div id="guest-subtab-msgs">
        <div style="background:#eef7ed;border:1px solid #d4edd2;border-radius:12px;padding:14px 16px;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px">
          <div>
            <b style="font-size:13px;color:var(--hm-primary)">⚡ Auto-filled with your Property Profile details</b>
            <p style="font-size:11.5px;color:var(--hm-muted);margin:2px 0 0">Switch between Hinglish, English, and Hindi for any situation with 1 click.</p>
          </div>
          <button class="hm-btn hm-btn-primary hm-btn-sm" id="btn-sync-profile-msgs" onclick="document.getElementById('btn-open-profile').click()">Edit Property Profile ↗</button>
        </div>

        <div id="hm-guest-messages-grid" class="hm-msg-grid"></div>
      </div>

      <!-- SUBTAB 2: PRINTABLE WELCOME STUDIO -->
      <div id="guest-subtab-studio" style="display:none">
        <div class="hm-studio-layout">
          <!-- Left: Input Form Panel -->
          <div class="hm-form-box">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
              <h3 style="font-size:16px;margin:0;color:var(--hm-primary)">Property Information</h3>
              <button class="hm-btn hm-btn-soft hm-btn-sm" id="btn-sync-profile-studio">Load Profile</button>
            </div>
            <p style="font-size:11.5px;color:var(--hm-muted);margin:0 0 16px">Details update the live preview instantly. Keep door access codes private.</p>

            <div class="hm-field-group">
              <label>Stay / Homestay Name</label>
              <input type="text" id="field-name" placeholder="e.g. The Himalayan Pine Villa">
            </div>

            <div class="hm-field-grid">
              <div class="hm-field-group">
                <label>Host / Family Name</label>
                <input type="text" id="field-host" placeholder="e.g. Rajesh & Aditi">
              </div>
              <div class="hm-field-group">
                <label>City & State</label>
                <input type="text" id="field-city" placeholder="e.g. Manali, Himachal">
              </div>
            </div>

            <div class="hm-field-grid">
              <div class="hm-field-group">
                <label>Check-in Time</label>
                <input type="text" id="field-checkin" placeholder="e.g. 2:00 PM onwards">
              </div>
              <div class="hm-field-group">
                <label>Checkout Time</label>
                <input type="text" id="field-checkout" placeholder="e.g. 11:00 AM">
              </div>
            </div>

            <div class="hm-field-grid">
              <div class="hm-field-group">
                <label>Wi-Fi Network SSID</label>
                <input type="text" id="field-wifi" placeholder="Network Name">
              </div>
              <div class="hm-field-group">
                <label>Wi-Fi Password</label>
                <input type="text" id="field-password" placeholder="Fill privately">
              </div>
            </div>

            <div class="hm-field-group">
              <label>Host Phone / Emergency WhatsApp</label>
              <input type="text" id="field-contact" placeholder="+91 98765 43210">
            </div>

            <div class="hm-field-group">
              <label>Welcome Greeting</label>
              <textarea id="field-greeting" rows="2" placeholder="We are happy to host you..."></textarea>
            </div>

            <div class="hm-field-group">
              <label>House Rules (One per line)</label>
              <textarea id="field-rules" rows="3" placeholder="Quiet hours: 10:30 PM...&#10;No smoking indoors..."></textarea>
            </div>

            <div class="hm-field-group">
              <label>Checkout Steps (One per line)</label>
              <textarea id="field-steps" rows="3" placeholder="Switch off geyser & heaters&#10;Return keys to caretaker"></textarea>
            </div>

            <div class="hm-field-group">
              <label>Local Recommendations (One per line)</label>
              <textarea id="field-local" rows="3" placeholder="Cafe 1947 - Best coffee (5 mins)&#10;Jogini Waterfall Hike (2 kms)"></textarea>
            </div>

            <div class="hm-field-group">
              <label>Warm Footer Note</label>
              <input type="text" id="field-note" placeholder="Wishing you a restful stay!">
            </div>
          </div>

          <!-- Right: Live Preview Panel -->
          <div class="hm-preview-box">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px">
              <h3 style="font-size:16px;margin:0;color:var(--hm-primary)">Live Printable Preview</h3>
              <div style="display:flex;gap:6px">
                <button class="hm-btn hm-btn-primary hm-btn-sm" id="btn-print-sheet">⎙ Print / Save PDF</button>
                <button class="hm-btn hm-btn-outline hm-btn-sm" id="btn-copy-sheet">Copy Text</button>
              </div>
            </div>

            <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px">
              <button class="hm-btn hm-btn-outline hm-btn-sm" data-template="welcome" aria-pressed="true">Welcome Sheet</button>
              <button class="hm-btn hm-btn-outline hm-btn-sm" data-template="wifi" aria-pressed="false">📶 In-Room Wi-Fi Card</button>
              <button class="hm-btn hm-btn-outline hm-btn-sm" data-template="rules" aria-pressed="false">House Rules</button>
              <button class="hm-btn hm-btn-outline hm-btn-sm" data-template="checkout" aria-pressed="false">Checkout List</button>
              <button class="hm-btn hm-btn-outline hm-btn-sm" data-template="local" aria-pressed="false">Local Guide</button>
            </div>

            <div class="hm-preview-stage">
              <div id="hm-print-sheet" class="hm-print-sheet"></div>
            </div>
            <p style="font-size:11px;color:var(--hm-muted);margin:10px 0 0;text-align:center">Printing Tip: Select Paper Size "A4" and enable "Background Graphics" in print dialog for crisp green accents.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SECTION 5: HOST RESOURCES & CALCULATOR ==================== -->
    <section class="hm-view" data-view="resources">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Finance · Strategy · Checklists</div>
          <h2>Host Resources & Pricing Calculator</h2>
          <p>Know your exact break-even nightly rate, simulate weekday vs weekend pricing, and track your 30-day host launch checklist.</p>
        </div>
      </div>

      <!-- PRICING & EXPENSE CALCULATOR -->
      <div class="hm-calc-grid" style="margin-bottom:28px">
        <!-- Inputs Column -->
        <div class="hm-calc-box">
          <h3 style="font-size:16px;font-weight:800;margin:0 0 6px;color:var(--hm-primary)">💰 Nightly Pricing & Expense Calculator</h3>
          <p style="font-size:12px;color:var(--hm-muted);margin:0 0 16px">Enter your monthly expenses in INR to find your minimum break-even and target pricing.</p>

          <div style="font-size:11.5px;font-weight:800;color:var(--hm-accent-dark);text-transform:uppercase;margin-bottom:8px">1. Monthly Fixed Costs (₹)</div>
          <div class="hm-field-grid">
            <div class="hm-field-group">
              <label>Rent / EMI / Lease</label>
              <input type="number" id="calc-fixed-rent" value="25000">
            </div>
            <div class="hm-field-group">
              <label>Electricity, Water & Wi-Fi</label>
              <input type="number" id="calc-fixed-util" value="5000">
            </div>
          </div>
          <div class="hm-field-grid">
            <div class="hm-field-group">
              <label>Caretaker / Staff Salary</label>
              <input type="number" id="calc-fixed-staff" value="8000">
            </div>
            <div class="hm-field-group">
              <label>Maintenance & Subscriptions</label>
              <input type="number" id="calc-fixed-other" value="2000">
            </div>
          </div>

          <div style="font-size:11.5px;font-weight:800;color:var(--hm-accent-dark);text-transform:uppercase;margin:12px 0 8px">2. Variable Turnover Costs per Booking (₹)</div>
          <div class="hm-field-grid">
            <div class="hm-field-group">
              <label>Linen Laundry per Turn</label>
              <input type="number" id="calc-var-laundry" value="400">
            </div>
            <div class="hm-field-group">
              <label>Deep Cleaning Supplies</label>
              <input type="number" id="calc-var-cleaning" value="300">
            </div>
          </div>
          <div class="hm-field-group">
            <label>Welcome Kit, Chai, Toiletries (per booking)</label>
            <input type="number" id="calc-var-welcome" value="250">
          </div>

          <div style="font-size:11.5px;font-weight:800;color:var(--hm-accent-dark);text-transform:uppercase;margin:12px 0 8px">3. Target Occupancy & Margin</div>
          <div class="hm-field-grid">
            <div class="hm-field-group">
              <label>Avg Stay (Nights)</label>
              <input type="number" id="calc-stay-nights" value="2.5" step="0.5">
            </div>
            <div class="hm-field-group">
              <label>Target Occupancy (%)</label>
              <input type="number" id="calc-occupancy" value="50" min="10" max="100">
            </div>
          </div>
          <div class="hm-field-group">
            <label>Desired Monthly Net Profit (₹)</label>
            <input type="number" id="calc-profit" value="35000">
          </div>
        </div>

        <!-- Outputs Column -->
        <div class="hm-calc-box" style="display:flex;flex-direction:column;justify-content:space-between">
          <div>
            <h3 style="font-size:16px;font-weight:800;margin:0 0 14px;color:var(--hm-primary)">📈 Recommended Pricing Strategy</h3>

            <div class="hm-calc-stat">
              <span style="text-transform:uppercase;font-size:10px;font-weight:800;letter-spacing:0.1em;color:var(--hm-accent-dark)">Minimum Break-Even Rate</span>
              <b id="calc-out-breakeven">₹2,840</b>
              <span>At this price, you cover 100% of operating expenses (zero profit). Never price below this.</span>
            </div>

            <div class="hm-calc-stat" style="background:#f0f9f3;border-color:#c8edd5">
              <span style="text-transform:uppercase;font-size:10px;font-weight:800;letter-spacing:0.1em;color:var(--hm-primary)">Recommended Base Weekday Rate (Mon–Thu)</span>
              <b id="calc-out-weekday" style="color:var(--hm-primary)">₹4,650</b>
              <span>Optimized for occupancy during mid-week workations & slow days.</span>
            </div>

            <div class="hm-calc-stat" style="background:#fffaf3;border-color:#fce4be">
              <span style="text-transform:uppercase;font-size:10px;font-weight:800;letter-spacing:0.1em;color:#b45309">Recommended Weekend Rate (Fri–Sun)</span>
              <b id="calc-out-weekend" style="color:#b45309">₹6,050</b>
              <span>Captures peak weekend leisure demand (+30% premium).</span>
            </div>

            <div style="font-size:12px;color:var(--hm-muted);padding:8px 0;line-height:1.6">
              • <b>Monthly Operating Costs:</b> <span id="calc-out-expenses">₹42,600</span><br>
              • <b>Estimated Nights Sold:</b> <span id="calc-out-nights">15 nights (50%)</span><br>
              • <b>Airbnb 3% Host Service Fee:</b> <span id="calc-out-fee">₹150 / night</span>
            </div>
          </div>

          <div style="background:#f4f7f2;border-radius:10px;padding:12px;font-size:11.5px;color:#3b4d45">
            <b>💡 Pricing Tip:</b> Festival dates (Diwali, New Year, Long Weekends) me weekend price se bhi 20-40% extra charge karein aur minimum 2-3 nights stay rule lagaayein.
          </div>
        </div>
      </div>

      <!-- 30-DAY MARKETING ACTION PLAN -->
      <div class="hm-checklist-box">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:14px">
          <div>
            <h3 style="margin:0 0 4px">📋 30-Day Marketing Action Plan for Beginners</h3>
            <p style="font-size:12px;color:var(--hm-muted);margin:0">Actionable daily checklist to launch, polish and scale your homestay's marketing.</p>
          </div>
          <div style="font-size:13px;font-weight:800;color:var(--hm-primary)" id="hm-plan-progress-label">0 of 20 Tasks Completed (0%)</div>
        </div>

        <!-- Progress Bar -->
        <div style="background:#edf1e8;height:8px;border-radius:99px;overflow:hidden;margin-bottom:20px">
          <div id="hm-plan-progress-bar" style="background:var(--hm-primary);width:0%;height:100%;transition:width 0.2s ease"></div>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px">
          <!-- Week 1 -->
          <div class="hm-plan-week">
            <h4>Week 1: Listing Foundation <span style="font-size:11px;color:var(--hm-muted)">Days 1–7</span></h4>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w1_1"><span>Perform 10-Point Listing Audit using HostMastery</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w1_2"><span>Rewrite listing title with unique differentiator</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w1_3"><span>Run internet speed test and take screenshot for listing</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w1_4"><span>Check bed configurations and disclose extra mattress rules</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w1_5"><span>Write pre-booking FAQs answering top 5 guest concerns</span></div>
          </div>

          <!-- Week 2 -->
          <div class="hm-plan-week">
            <h4>Week 2: Photography & Staging <span style="font-size:11px;color:var(--hm-muted)">Days 8–14</span></h4>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w2_1"><span>Steam iron white bedsheets and fluff pillows</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w2_2"><span>Shoot 5 golden-hour photos of balcony and living area</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w2_3"><span>Take clean bathroom shot showing geyser and toiletries</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w2_4"><span>Rearrange first 5 listing photos in golden sequence</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w2_5"><span>Add alt-text and captions to all 25+ listing photos</span></div>
          </div>

          <!-- Week 3 -->
          <div class="hm-plan-week">
            <h4>Week 3: Social & Video Vault <span style="font-size:11px;color:var(--hm-muted)">Days 15–21</span></h4>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w3_1"><span>Film 30-second room-by-room walkthrough video</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w3_2"><span>Record aesthetic no-face morning tea/view clip</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w3_3"><span>Post Reel using Hook #1 with link in bio to Airbnb</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w3_4"><span>Create 7-slide "Things to know before booking" carousel</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w3_5"><span>Save local food & sightseeing spots in Instagram Highlights</span></div>
          </div>

          <!-- Week 4 -->
          <div class="hm-plan-week">
            <h4>Week 4: Guest Experience & Reviews <span style="font-size:11px;color:var(--hm-muted)">Days 22–30</span></h4>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w4_1"><span>Print and frame Wi-Fi Information Card for bedside</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w4_2"><span>Print laminated House Rules & Checkout Checklist</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w4_3"><span>Test pre-arrival WhatsApp template on next booking</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w4_4"><span>Send mid-stay comfort message ("Sab theek hai?")</span></div>
            <div class="hm-check-row"><input type="checkbox" data-plan-task="w4_5"><span>Send polite 5-star review request after guest departs</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SECTION 6: LEARN & IMPROVE ==================== -->
    <section class="hm-view" data-view="academy">
      <div class="hm-section-title-bar">
        <div>
          <div class="hm-kicker">Knowledge · Academy · Best Practices</div>
          <h2>Learn & Improve (Host Academy)</h2>
          <p>Clear, practical guides on AI prompt engineering for hosts, smartphone photography, handling difficult guests, and Indian homestay regulations.</p>
        </div>
      </div>

      <div class="hm-academy-grid">
        <!-- Module 1 -->
        <article class="hm-academy-card">
          <div class="hm-pill-cat" style="margin-bottom:8px">Module 01</div>
          <h3>AI Prompting Masterclass for Hosts</h3>
          <p style="font-size:12px;color:var(--hm-muted);line-height:1.6">How to get genuine, high-converting copy from ChatGPT or Gemini instead of generic travel fluff:</p>
          <div class="hm-academy-step">
            <div class="hm-step-badge">1</div>
            <div style="font-size:12px"><b>Give Property Facts First:</b> Always specify exact room dimensions, real bed sizes, and verified distances. Never let AI guess.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">2</div>
            <div style="font-size:12px"><b>Specify the Indian Context:</b> Instruct: <i>"Write in warm, hospitable Indian English (or Hinglish) suitable for families and young travelers."</i></div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">3</div>
            <div style="font-size:12px"><b>Forbid Unverified Superlatives:</b> Explicitly tell the AI: <i>"Do not use words like 'luxurious', 'best in town', or 'hidden gem' unless substantiated."</i></div>
          </div>
        </article>

        <!-- Module 2 -->
        <article class="hm-academy-card">
          <div class="hm-pill-cat" style="margin-bottom:8px">Module 02</div>
          <h3>Smartphone Photography & Staging</h3>
          <p style="font-size:12px;color:var(--hm-muted);line-height:1.6">You don't need a ₹1,00,000 camera to win bookings. Follow these smartphone rules:</p>
          <div class="hm-academy-step">
            <div class="hm-step-badge">✓</div>
            <div style="font-size:12px"><b>Turn on All Warm Lights:</b> Switch on bedside lamps and ceiling fixtures even during the daytime for a warm, cozy glow.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">✓</div>
            <div style="font-size:12px"><b>Shoot from Waist Height:</b> Holding the phone at chest/waist level keeps vertical wall lines straight and rooms looking natural.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">✓</div>
            <div style="font-size:12px"><b>Avoid Ultra-Wide Distortion:</b> 0.5x ultra-wide makes rooms look unnaturally huge, leading to guest disappointment and bad reviews. Use 1x and step back.</div>
          </div>
        </article>

        <!-- Module 3 -->
        <article class="hm-academy-card">
          <div class="hm-pill-cat" style="margin-bottom:8px">Module 03</div>
          <h3>Handling Difficult Hosting Realities</h3>
          <p style="font-size:12px;color:var(--hm-muted);line-height:1.6">How to handle unexpected issues calmly and protect your 5-star rating:</p>
          <div class="hm-academy-step">
            <div class="hm-step-badge">⚡</div>
            <div style="font-size:12px"><b>Sudden Power Cuts:</b> Message the guest immediately <i>before</i> they message you. Inform them about inverter capacity and estimated restoration time.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">⚡</div>
            <div style="font-size:12px"><b>Late Check-in Demands:</b> Install a simple digital key lockbox so guests arriving at 2:00 AM can self check-in seamlessly.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">⚡</div>
            <div style="font-size:12px"><b>Quiet Hour Violations:</b> Have your on-site caretaker offer a gentle verbal reminder rather than an aggressive confrontation.</div>
          </div>
        </article>

        <!-- Module 4 -->
        <article class="hm-academy-card">
          <div class="hm-pill-cat" style="margin-bottom:8px">Module 04</div>
          <h3>Indian Homestay Regulations & Trust</h3>
          <p style="font-size:12px;color:var(--hm-muted);line-height:1.6">Legal & regulatory essentials for peaceful hosting in India:</p>
          <div class="hm-academy-step">
            <div class="hm-step-badge">📋</div>
            <div style="font-size:12px"><b>Government ID Verification:</b> Collect Aadhaar / Passport details via a secure digital form prior to or upon physical check-in.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">📋</div>
            <div style="font-size:12px"><b>C-Form for Foreign Guests:</b> Mandatory registration on the Indian Bureau of Immigration BoI portal within 24 hours of arrival.</div>
          </div>
          <div class="hm-academy-step">
            <div class="hm-step-badge">📋</div>
            <div style="font-size:12px"><b>Fire Safety & First Aid:</b> Keep an active ABC dry-powder fire extinguisher and stocked first-aid kit visibly accessible.</div>
          </div>
        </article>
      </div>
    </section>

    <!-- FOOTER -->
    <footer style="margin-top:36px;padding:24px 0 12px;border-top:1px solid var(--hm-line);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;font-size:11.5px;color:var(--hm-muted)">
      <div><b>HostMastery</b> · The All-in-One Airbnb Host Kit for Indian Homestays & Stays.</div>
      <div>Prompts are starting points. Always verify facts and local requirements.</div>
    </footer>

    <!-- EMBEDDED PROMPT DATA - SAFELY INSIDE #hm-app -->
    <script type="application/json" id="hm-prompt-data">
{prompts_json_escaped}
    </script>

  </div>

  <!-- ==================== MODALS ==================== -->
  
  <!-- 1. PROPERTY PROFILE MODAL -->
  <div id="hm-modal-profile" class="hm-modal-backdrop">
    <div class="hm-modal-card">
      <button class="hm-modal-close" data-close-modal>✕</button>
      <h3 style="font-size:18px;font-weight:850;margin:0 0 6px;color:var(--hm-primary)">🏠 My Property Profile</h3>
      <p style="font-size:12px;color:var(--hm-muted);margin:0 0 18px">Save your details once. They automatically auto-populate Welcome Studio sheets, personalize all 340+ prompts, and customize guest messages!</p>

      <div class="hm-field-group">
        <label>Property / Homestay Name</label>
        <input type="text" id="modal-prof-name" placeholder="e.g. The Himalayan Pine Villa">
      </div>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>Host / Brand Name</label>
          <input type="text" id="modal-prof-host" placeholder="e.g. Rajesh & Aditi">
        </div>
        <div class="hm-field-group">
          <label>City & State</label>
          <input type="text" id="modal-prof-city" placeholder="e.g. Manali, Himachal Pradesh">
        </div>
      </div>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>Property Type</label>
          <input type="text" id="modal-prof-type" placeholder="e.g. Boutique Mountain Homestay">
        </div>
        <div class="hm-field-group">
          <label>Target Guests</label>
          <input type="text" id="modal-prof-guests" placeholder="e.g. Couples, Families & Workationers">
        </div>
      </div>

      <div class="hm-field-group">
        <label>Standout Verified Amenities (comma-separated)</label>
        <input type="text" id="modal-prof-amenities" placeholder="e.g. 100 Mbps Wi-Fi, Mountain View Balcony, Bonfire, Home-cooked Food">
      </div>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>Check-in Time</label>
          <input type="text" id="modal-prof-checkin" placeholder="e.g. 2:00 PM onwards">
        </div>
        <div class="hm-field-group">
          <label>Checkout Time</label>
          <input type="text" id="modal-prof-checkout" placeholder="e.g. 11:00 AM">
        </div>
      </div>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>In-Room Wi-Fi SSID</label>
          <input type="text" id="modal-prof-wifi" placeholder="Network Name">
        </div>
        <div class="hm-field-group">
          <label>Wi-Fi Password</label>
          <input type="text" id="modal-prof-password" placeholder="Password">
        </div>
      </div>

      <div class="hm-field-group">
        <label>Host Phone / Emergency WhatsApp</label>
        <input type="text" id="modal-prof-contact" placeholder="+91 98765 43210">
      </div>

      <div style="display:flex;justify-content:flex-end;gap:8px;margin-top:16px">
        <button class="hm-btn hm-btn-outline" data-close-modal>Cancel</button>
        <button class="hm-btn hm-btn-primary" id="btn-save-profile">Save & Apply Everywhere ✓</button>
      </div>
    </div>
  </div>

  <!-- 2. CUSTOM PROMPT WIZARD MODAL -->
  <div id="hm-modal-wizard" class="hm-modal-backdrop">
    <div class="hm-modal-card">
      <button class="hm-modal-close" data-close-modal>✕</button>
      <h3 style="font-size:18px;font-weight:850;margin:0 0 6px;color:var(--hm-primary)">⚡ 10,000+ Custom Prompt Wizard</h3>
      <p style="font-size:12px;color:var(--hm-muted);margin:0 0 16px">Select your parameters to instantly generate a tailored master prompt in Hinglish or English.</p>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>Property Category</label>
          <select id="wiz-type">
            <option value="Mountain Homestay">Mountain Homestay / Cabin</option>
            <option value="Luxury Private Villa">Luxury Private Villa with Pool</option>
            <option value="Heritage Haveli / Traditional Home">Heritage Haveli / Traditional Home</option>
            <option value="City Studio Apartment / Workation Flat">City Studio Apartment / Workation Flat</option>
            <option value="Countryside Farmhouse">Countryside Farmhouse / Estate</option>
            <option value="Coastal Beach Cottage">Coastal Beach Cottage</option>
          </select>
        </div>
        <div class="hm-field-group">
          <label>Target Audience</label>
          <select id="wiz-audience">
            <option value="Couples & Honeymooners">Couples & Honeymooners</option>
            <option value="Families with Kids & Elders">Families with Kids & Elders</option>
            <option value="Remote Workers / Workationers">Remote Workers / Workationers</option>
            <option value="Weekend Friend Groups & Road-trippers">Weekend Friend Groups & Road-trippers</option>
            <option value="Solo Travelers & Explorers">Solo Travelers & Explorers</option>
          </select>
        </div>
      </div>

      <div class="hm-field-grid">
        <div class="hm-field-group">
          <label>Marketing Goal</label>
          <select id="wiz-goal">
            <option value="Instagram Reel Script & Visual Cues">Instagram Reel Script & Visual Cues</option>
            <option value="High-Converting Airbnb Listing Description">High-Converting Airbnb Listing Description</option>
            <option value="20 Irresistible Listing Titles">20 Irresistible Listing Titles</option>
            <option value="Pre-Booking Guest FAQ Section">Pre-Booking Guest FAQ Section</option>
            <option value="Weekend Promotional Offer Creative">Weekend Promotional Offer Creative</option>
            <option value="Local Area Insider Guide">Local Area Insider Guide</option>
          </select>
        </div>
        <div class="hm-field-group">
          <label>Tone of Voice</label>
          <select id="wiz-tone">
            <option value="Warm & Hospitable Conversational Hinglish">Warm & Hospitable Conversational Hinglish</option>
            <option value="Modern, Minimal & Practical">Modern, Minimal & Practical</option>
            <option value="Aesthetic & Poetic Luxury">Aesthetic & Poetic Luxury</option>
            <option value="Adventure & Nature Focused">Adventure & Nature Focused</option>
          </select>
        </div>
      </div>

      <button class="hm-btn hm-btn-coral" style="width:100%;margin-top:10px" id="btn-generate-wizard">Generate Bespoke Prompt ✦</button>

      <div id="wiz-output-box" style="display:none;margin-top:16px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <b style="font-size:12.5px;color:var(--hm-primary)">Generated Master Prompt:</b>
          <button class="hm-btn hm-btn-primary hm-btn-sm" id="wiz-copy-btn">📋 Copy Prompt</button>
        </div>
        <pre style="background:#f7faf5;border:1px solid #e1e7dc;border-radius:10px;padding:12px;font-size:11.5px;line-height:1.6;max-height:220px;overflow-y:auto;white-space:pre-wrap;color:#2c3d35;margin:0"></pre>
      </div>
    </div>
  </div>

  <!-- 3. PERSONALIZE PROMPT MODAL -->
  <div id="hm-modal-personalize" class="hm-modal-backdrop">
    <div class="hm-modal-card">
      <button class="hm-modal-close" data-close-modal>✕</button>
      <h3 style="font-size:18px;font-weight:850;margin:0 0 4px;color:var(--hm-primary)" id="pers-modal-title">Personalize Prompt</h3>
      <p style="font-size:12px;color:var(--hm-muted);margin:0 0 14px">Your property details have been automatically inserted into this prompt:</p>
      <pre id="pers-modal-preview" style="background:#f7faf5;border:1px solid #e1e7dc;border-radius:10px;padding:12px;font-size:11.5px;line-height:1.6;max-height:260px;overflow-y:auto;white-space:pre-wrap;color:#2c3d35;margin:0 0 16px"></pre>
      <div style="display:flex;justify-content:flex-end;gap:8px">
        <button class="hm-btn hm-btn-outline" data-close-modal>Close</button>
        <button class="hm-btn hm-btn-primary" id="pers-modal-copy">📋 Copy Personalized Prompt</button>
      </div>
    </div>
  </div>

  <!-- 4. EXPORT MARKETING KIT MODAL -->
  <div id="hm-modal-export" class="hm-modal-backdrop">
    <div class="hm-modal-card">
      <button class="hm-modal-close" data-close-modal>✕</button>
      <h3 style="font-size:18px;font-weight:850;margin:0 0 4px;color:var(--hm-primary)">📦 Export Your Complete Marketing Kit</h3>
      <p style="font-size:12px;color:var(--hm-muted);margin:0 0 14px">Download your organized property facts, welcome sheets, and guest templates as a Markdown document.</p>
      <pre id="export-kit-preview" style="background:#f7faf5;border:1px solid #e1e7dc;border-radius:10px;padding:12px;font-size:11.5px;line-height:1.6;max-height:260px;overflow-y:auto;white-space:pre-wrap;color:#2c3d35;margin:0 0 16px"></pre>
      <div style="display:flex;justify-content:flex-end;gap:8px">
        <button class="hm-btn hm-btn-outline" data-close-modal>Close</button>
        <button class="hm-btn hm-btn-primary" id="btn-download-export-md">💾 Download Markdown (.md)</button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="hm-toast" class="hm-toast" role="status" aria-live="polite">Copied to clipboard ✓</div>

  <!-- MOBILE FIXED BOTTOM NAV BAR -->
  <nav class="hm-mobile-bar" aria-label="Mobile Navigation">
    <button class="hm-mbar-btn hm-active" data-tab="prompts">
      <span class="hm-mbar-icon">✦</span>
      <span>Prompts</span>
    </button>
    <button class="hm-mbar-btn" data-tab="growth">
      <span class="hm-mbar-icon">🚀</span>
      <span>Growth</span>
    </button>
    <button class="hm-mbar-btn" data-tab="social">
      <span class="hm-mbar-icon">📱</span>
      <span>Social</span>
    </button>
    <button class="hm-mbar-btn" data-tab="guest">
      <span class="hm-mbar-icon">🤝</span>
      <span>Guest</span>
    </button>
    <button class="hm-mbar-btn" data-tab="resources">
      <span class="hm-mbar-icon">📊</span>
      <span>Calc</span>
    </button>
    <button class="hm-mbar-btn" data-tab="academy">
      <span class="hm-mbar-icon">🎓</span>
      <span>Learn</span>
    </button>
  </nav>

</div>
"""

# Global Helper Functions
GLOBAL_HELPERS_JS = """
window.switchGuestSubtab = function(tab) {
  const msgs = document.getElementById('guest-subtab-msgs');
  const studio = document.getElementById('guest-subtab-studio');
  const btnMsgs = document.getElementById('subtab-btn-msgs');
  const btnStudio = document.getElementById('subtab-btn-studio');
  if (tab === 'msgs') {
    if (msgs) msgs.style.display = 'block';
    if (studio) studio.style.display = 'none';
    if (btnMsgs) { btnMsgs.className = 'hm-btn hm-btn-soft'; }
    if (btnStudio) { btnStudio.className = 'hm-btn hm-btn-outline'; }
  } else {
    if (msgs) msgs.style.display = 'none';
    if (studio) studio.style.display = 'block';
    if (btnMsgs) { btnMsgs.className = 'hm-btn hm-btn-outline'; }
    if (btnStudio) { btnStudio.className = 'hm-btn hm-btn-soft'; }
  }
};

window.copyScript = function(type) {
  let text = '';
  if (type === '30sec') {
    text = `🎬 30-Second Scenic Property Tour Reel Script
Audio: Trending acoustic/chill indie track (e.g. soothing flute / guitar).
[0:00 - 0:03] Hook: Hand pushing open balcony door with steaming chai cup. Text on screen: "Finding peace in [City] hits different here."
[0:03 - 0:10] Bedroom: Smooth slow-mo pan of pristine white bed, fluffy pillows, natural morning light pouring in.
[0:10 - 0:18] Standout Amenity: Cozy dedicated workstation with scenic view or evening bonfire setup.
[0:18 - 0:25] Spotless Washroom: 2-second crisp pan showing clean tiles, hot geyser, fluffy rolled towels.
[0:25 - 0:30] Golden Hour Balcony & CTA: "Your peaceful weekend escape awaits. Link in bio to check dates on Airbnb!"
Caption: Escape the city chaos. Save this for your next [City] road trip! 🌿 #homestayindia #airbnbindia #weekendgetaway`;
  } else {
    text = `🎬 Aesthetic POV Workation Reel Script
Audio: Lo-fi ambient rain / acoustic beats.
Visual 1: Opening laptop on wooden desk with panoramic hill/garden view.
Visual 2: 100 Mbps Wi-Fi speed test shown on smartphone screen.
Visual 3: Pouring fresh hot filter coffee or masala chai into ceramic mug.
On-screen text: "Taking Zoom calls with this view is my new non-negotiable."
Caption: Work from wherever your soul feels peaceful. 100 Mbps Wi-Fi, mountain air, and home-cooked meals. 📍 [Property Name]. Tap link in bio to book!`;
  }
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text);
    const t = document.getElementById('hm-toast');
    if (t) {
      t.textContent = 'Reel Script Copied to Clipboard ✓';
      t.classList.add('hm-show');
      setTimeout(() => t.classList.remove('hm-show'), 2400);
    }
  }
};

window.renderHooks = function(cat) {
  const list = document.getElementById('hm-hooks-list');
  if (list && window.renderViralHooksInternal) {
    window.renderViralHooksInternal(cat);
  }
};
"""

# 1. GENERATE INDEX.HTML
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>HostMastery — The All-in-One Airbnb Host Kit for Indian Hosts & Homestays</title>
  <meta name="description" content="340+ AI Prompts, 10,000+ Combinations Prompt Matrix, Listing Audit Tool, Reels Vault, Hinglish Guest Messages, and Printable Welcome Studio for Indian Airbnb Hosts.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;850&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
{css_content}
  </style>
</head>
<body>
{HTML_BODY}

  <!-- Global helper functions -->
  <script>
{GLOBAL_HELPERS_JS}
  </script>

  <!-- Main Application Logic -->
  <script>
{js_content}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print(f"Generated index.html successfully ({len(index_html)} bytes).")

# 2. GENERATE HOSTMASTERY_EMBED.HTML
embed_html = f"""<!-- HostMastery | All-in-One Airbnb Host Kit | Self-contained Google Sites embed -->
<div id="hm-app" class="hm-app">
  <style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;850&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
{css_content}
  </style>

{HTML_BODY}

  <!-- Global helper functions -->
  <script>
{GLOBAL_HELPERS_JS}
  </script>

  <!-- Main Application Logic -->
  <script>
{js_content}
  </script>
</div>
"""

with open('hostmastery_embed.html', 'w', encoding='utf-8') as f:
    f.write(embed_html)
print(f"Generated hostmastery_embed.html successfully ({len(embed_html)} bytes).")
