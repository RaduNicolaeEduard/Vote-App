<template>
  <v-app>
    <v-progress-linear indeterminate v-if="$store.getters.loading" style="z-index:1000; position:fixed;"></v-progress-linear>
    <appnavbar/>
    <v-main>
      <pre v-if="$keycloak.authenticated == true && $keycloak.tokenParsed.hasOwnProperty('profile_setup') && $keycloak.tokenParsed.profile_setup== true">
        {{ $keycloak }}
      </pre>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import appnavbar from '@/components/app-nav-bar.vue'
export default {
  name: 'App',
  components: {
    appnavbar,
    },
  methods: {
  },
  data: () => ({
  }),
};
</script>
