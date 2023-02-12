<template>
  <div>
    <v-container class="landing-page" fluid>
      <v-content>
        <v-parallax class="elevation-12" src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg" height="600">
          <v-layout column align-center justify-center class="white--text text-center">
            <h1 class="display-2 mb-3">Welcome to Vote</h1>
            <p class="subtitle-1">Cast your vote for your preferred candidate today!</p>
            <div>

              <v-btn class="ma-3 white--text" color="primary" @click="getData()" dark>
                Start Voting
              </v-btn>
              <v-btn class="ma-3 white--text" color="primary" @click="register()" dark>
                Register Today
              </v-btn>
            </div>
          </v-layout>
        </v-parallax>
        <v-container>
          <section>
            <v-row>
              <v-col cols="12" md="4">
                <v-card class="elevation-12">
                  <v-card-title>Section 1</v-card-title>
                  <v-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Sed a augue non justo fringilla bibendum.
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="4">
                <v-card class="elevation-12">
                  <v-card-title>Section 2</v-card-title>
                  <v-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Sed a augue non justo fringilla bibendum.
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="4">
                <v-card class="elevation-12">
                  <v-card-title>Section 3</v-card-title>
                  <v-card-text>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Sed a augue non justo fringilla bibendum.
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </section>
        </v-container>
      </v-content>
    </v-container>
    <v-footer>
      <v-container >
        <v-row>
          <v-col>
            <v-btn text href="#about">About Us</v-btn>
            <v-btn text href="#services">Services</v-btn>
            <v-btn text href="#blog">Blog</v-btn>
          </v-col>
          <v-spacer></v-spacer>
          <v-col>
            <v-btn text href="#faq">FAQ</v-btn>
            <v-btn text href="#privacy">Privacy Policy</v-btn>
            <v-btn text href="#terms">Terms and Conditions</v-btn>
          </v-col>
        </v-row>
        <v-divider class="my-3"></v-divider>
        <v-row class="text-center">
          <v-col cols="12">
            <span>Copyright © {{ new Date().getFullYear() }} Vote</span>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    }
  },
  methods: {
    register() {
      this.$keycloak.register();
    },
    async getData() {
      try {
        const response = await this.$http.get(
          `${process.env.VUE_APP_BASE_URL}/elections`
        );
        // JSON responses are automatically parsed.
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  components: {
  },
}
</script>
