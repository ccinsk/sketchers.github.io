# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='index', parent='pages')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404

# Pages -- Landing pages

@app.route('/pages/presentation/')
def pages_presentation():
  return render_template('pages/presentation.html', segment='presentation', parent='pages')

@app.route('/pages/about-us/')
def pages_about_us():
  return render_template('pages/about-us.html', segment='about_us', parent='pages')

@app.route('/pages/contact-us/')
def pages_contact_us():
  return render_template('pages/contact-us.html', segment='contact_us', parent='pages')

@app.route('/pages/author/')
def pages_author():
  return render_template('pages/author.html', segment='author', parent='pages')

# Pages -- Account

@app.route('/accounts/sign-in/')
def accounts_sign_in():
  return render_template('accounts/sign-in.html', segment='sign_in', parent='accounts')

@app.route('/accounts/sign-up/')
def accounts_sign_up():
  return render_template('accounts/sign-up.html', segment='sign-up', parent='accounts')

# Sections -- Page sections

@app.route('/sections/page-sections/hero-sections/')
def sections_page_sections_hero_sections():
  return render_template('sections/page-sections/hero-sections.html', segment='hero_sections', parent='sections')

@app.route('/sections/page-sections/features/')
def sections_page_sections_features():
  return render_template('sections/page-sections/features.html', segment='features', parent='sections')

# Sections -- Navigation

@app.route('/sections/navigation/navbars/')
def sections_navigation_navbars():
  return render_template('sections/navigation/navbars.html', segment='navbars', parent='sections')

@app.route('/sections/navigation/nav-tabs/')
def sections_navigation_nav_tabs():
  return render_template('sections/navigation/nav-tabs.html', segment='nav_tabs', parent='sections')

@app.route('/sections/navigation/pagination/')
def sections_navigation_pagination():
  return render_template('sections/navigation/pagination.html', segment='pagination', parent='sections')

# Sections -- Input area

@app.route('/sections/input-areas/inputs/')
def sections_input_areas_inputs():
  return render_template('sections/input-areas/inputs.html', segment='inputs', parent='sections')

@app.route('/sections/input-areas/forms/')
def sections_input_areas_forms():
  return render_template('sections/input-areas/forms.html', segment='forms', parent='sections')

# Sections -- attention-catchers

@app.route('/sections/attention-catchers/alerts/')
def sections_attention_catchers_alerts():
  return render_template('sections/attention-catchers/alerts.html', segment='alerts', parent='sections')

@app.route('/sections/attention-catchers/modals/')
def sections_attention_catchers_modals():
  return render_template('sections/attention-catchers/modals.html', segment='modals', parent='sections')

@app.route('/sections/attention-catchers/tooltips-popovers/')
def sections_attention_catchers_tooltips_popovers():
  return render_template('sections/attention-catchers/tooltips-popovers.html', segment='tooltips_popovers', parent='sections')

# Sections -- elements

@app.route('/sections/elements/avatars/')
def sections_elements_avatars():
  return render_template('sections/elements/avatars.html', segment='avatars', parent='sections')

@app.route('/sections/elements/badges/')
def sections_elements_badges():
  return render_template('sections/elements/badges.html', segment='badges', parent='sections')

@app.route('/sections/elements/breadcrumbs/')
def sections_elements_breadcrumbs():
  return render_template('sections/elements/breadcrumbs.html', segment='breadcrumbs', parent='sections')

@app.route('/sections/elements/buttons/')
def sections_elements_buttons():
  return render_template('sections/elements/buttons.html', segment='buttons', parent='sections')

@app.route('/sections/elements/dropdowns/')
def sections_elements_dropdowns():
  return render_template('sections/elements/dropdowns.html', segment='dropdowns', parent='sections')

@app.route('/sections/elements/progress-bars/')
def sections_elements_progress_bars():
  return render_template('sections/elements/progress-bars.html', segment='progress_bars', parent='sections')

@app.route('/sections/elements/toggles/')
def sections_elements_toggles():
  return render_template('sections/elements/toggles.html', segment='toggles', parent='sections')

@app.route('/sections/elements/typography/')
def sections_elements_typography():
  return render_template('sections/elements/typography.html', segment='typography', parent='sections')
