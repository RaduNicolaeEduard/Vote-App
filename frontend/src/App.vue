<template>
  <v-app>
    <v-progress-linear indeterminate v-if="$store.getters.loading" style="z-index:1000; position:fixed;"></v-progress-linear>
    <appnavbar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
console.log(process.env)
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
