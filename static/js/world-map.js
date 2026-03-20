/**
 * world-map.js — Homepage world map (jsvectormap)
 * Highlights 26+ countries Vaible Herbal exports to.
 */
(function () {
  'use strict';

  if (typeof jsVectorMap === 'undefined') return;

  const SERVED_COUNTRIES = [
    // Europe
    'GB', 'DE', 'FR', 'NL', 'IT', 'ES', 'CH', 'PL', 'BE', 'SE', 'AT', 'DK',
    // Americas
    'US', 'CA', 'BR', 'MX',
    // Middle East
    'AE', 'SA', 'QA', 'KW',
    // Asia-Pacific
    'JP', 'KR', 'SG', 'AU', 'NZ', 'MY',
    // Africa
    'ZA', 'NG',
    // South Asia (home + neighbours)
    'IN',
  ];

  new jsVectorMap({
    selector: '#worldMap',
    map: 'world',
    backgroundColor: 'transparent',
    zoomButtons: false,
    zoomOnScroll: false,
    draggable: false,

    regionStyle: {
      initial: {
        fill: '#1a3d2b',
        stroke: '#0d2418',
        strokeWidth: 0.5,
      },
      hover: {
        fill: '#4ade80',
        fillOpacity: 1,
        cursor: 'default',
      },
      selected: {
        fill: '#4ade80',
      },
      selectedHover: {
        fill: '#86efac',
      },
    },

    selectedRegions: SERVED_COUNTRIES,

    onRegionTooltipShow(event, tooltip, code) {
      if (!SERVED_COUNTRIES.includes(code)) {
        event.preventDefault();
      }
    },
  });

})();
