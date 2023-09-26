import injector
import careers
import world
import event_testing
import world.region
import build_buy
import services
import os, logging
from careers import career_event


POLICE_STATION_VENUE_TUNING_ID = 109774


@injector.inject(careers.career_event.CareerEvent, 'on_career_event_requested')
def _on_career_event_requested(original, self):
    required_zone_id = self.required_zone.get_required_zone_id(self.sim_info)
    required_venue_tuning_id = build_buy.get_current_venue(required_zone_id)

    if required_venue_tuning_id != POLICE_STATION_VENUE_TUNING_ID:
        original(self)
        return

    household_zone_id = self.sim_info.household.home_zone_id
    region_id = world.region.get_region_description_id_from_zone_id(household_zone_id)

    neighbourhood_zone_ids = []
    persistence_service = services.get_persistence_service()
    for zone_data in persistence_service.zone_proto_buffs_gen():
        zone_id = zone_data.zone_id
        world_id = zone_data.world_id
        if persistence_service.get_region_id_from_world_id(world_id) == region_id:
            neighbourhood_zone_ids.append(zone_id)

    local_police_station_zone_id = -1

    for zone_id in neighbourhood_zone_ids:
        venue_tuning_id = build_buy.get_current_venue(zone_id)
        if venue_tuning_id == POLICE_STATION_VENUE_TUNING_ID:
            local_police_station_zone_id = zone_id
            break

    self._advance_state(careers.career_event.CareerEventState.REQUESTED)
    self._required_zone_id = local_police_station_zone_id if local_police_station_zone_id > 0 else required_zone_id

    if self.subvenue:
        services.get_career_service().start_career_event_subvenue(self, self._required_zone_id, self.subvenue.venue)
    if self.loot_on_request is not None:
        resolver = event_testing.resolver.SingleSimResolver(self._career.sim_info)
        self.loot_on_request.apply_to_resolver(resolver)
