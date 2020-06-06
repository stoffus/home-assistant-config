entity_id = data.get('entity_id')
media_player_state = hass.states.get(entity_id)
target_source = 'Viaplay'
target_volume = 0.10
menu_total_items = 10
menu_kids_section_index = -3
menu_seek_start_top = menu_kids_section_index > 0

if media_player_state.state != 'off':
  hass.services.call('media_player', 'turn_off', { 'entity_id': entity_id }, True)
  time.sleep(5)

hass.services.call('media_player', 'turn_on', { 'entity_id': entity_id }, True)

time.sleep(2)

if media_player_state.source != target_source:
  logger.info('Correcting source')
  hass.services.call('media_player', 'select_source', { 'entity_id': entity_id, 'source': target_source }, True)

time.sleep(15)

#logger.info('Choosing a profile')
#hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'ENTER' }, True)
#time.sleep(7)

logger.info('Entering main menu')

# Show main menu
hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'BACK' }, True)

# Make sure the menu commands starts at the right index
menu_go_to_beginning_button = 'UP' if menu_kids_section_index >= 0 else 'DOWN'

logger.info('Going to the top or bottom')

for i in range(menu_total_items - 1):
  hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': menu_go_to_beginning_button }, True)
  #time.sleep(0.1)

menu_go_to_section_button = 'DOWN' if menu_kids_section_index >= 0 else 'UP'

logger.info('Going to the correct section')

for i in range(abs(menu_kids_section_index)):
  hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': menu_go_to_section_button }, True)
  #time.sleep(0.1)

# Select the kids section
hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'ENTER' }, True)

time.sleep(5)

# Navigate down to the recently played section
hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'DOWN' }, True)

time.sleep(3)

# Select the first item in the list
hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'ENTER' }, True)

time.sleep(5)

# Now play it!
#hass.services.call('webostv', 'button', { 'entity_id': entity_id, 'button': 'ENTER' }, True)

time.sleep(1)

# Set a reasonable volume
hass.services.call('media_player', 'volume_set', { 'entity_id': entity_id, 'volume_level': target_volume }, True)
