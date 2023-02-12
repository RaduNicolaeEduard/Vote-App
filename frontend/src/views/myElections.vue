<template>
    <v-container>
        <div class="text-center">
            <!-- Create new election button -->
            <template>
                    <v-dialog v-model="dialog" fullscreen  transition="dialog-bottom-transition">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn v-bind="attrs" v-on="on">
                                Create Election
                            </v-btn>
                        </template>
                        <v-card>
                            <v-toolbar dark color="primary">
                                <v-btn icon dark @click="dialog = false">
                                    <v-icon>mdi-close</v-icon>
                                </v-btn>
                                <v-toolbar-title>Create Election</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-toolbar-items>
                                    <v-btn dark text @click="createElection">
                                        Submit
                                    </v-btn>
                                </v-toolbar-items>
                            </v-toolbar>
                            <v-container>

                                <v-form>
                                    <!-- Photo -->
                                    <v-file-input
                                        label="Election Photo"
                                        prepend-icon="mdi-camera"
                                        v-model="file"
                                    ></v-file-input>
                                    <v-text-field
                                        v-model="name"
                                        label="Name"
                                        required
                                    ></v-text-field>
                                    <v-text-field
                                        label="Description"
                                        v-model="description"
                                        required
                                    ></v-text-field>
                                    <v-text-field
                                        label="Candidates"
                                        v-model="candidates"
                                        required
                                    ></v-text-field>
                                    <v-select
                                        :items="['Local', 'National']"
                                        label="Election Type"
                                        v-model="electionType"
                                        required
                                    ></v-select>
                                    <!-- Geo Restriction for voters -->
                                    <v-select
                                        :items="['Yes', 'No']"
                                        label="Geo Restriction"
                                        v-model="geoRestriction"
                                        required
                                    ></v-select>
                                    <v-autocomplete
                                        v-if="geoRestriction === 'Yes'"
                                        v-model="contry"
                                        :items="countriesArr"
                                        label="Contry"
                                    ></v-autocomplete>
                                    <v-autocomplete
                                        v-if="geoRestriction === 'Yes'"
                                        v-model="state"
                                        :items="stateArr"
                                        label="State"
                                    ></v-autocomplete>
                                    <pre>
                                        {{ file }}
                                    </pre>
                                </v-form>
                            </v-container>
                        </v-card>
                    </v-dialog>
            </template> 
            <v-divider class="my-3"></v-divider>
            <div>
                <electioncard />
            </div>
        </div>
    </v-container>
</template>

<script>
import countires from '@/assets/countires.json'
import electioncard from '../components/vote-card.vue'
export default {
    components: {
        electioncard
    },
    name: 'vote-card',

    data: () => ({
        tab: null,
        dialog: true,
        date: null,
        file: null,
        name: null,
        countriesArr: [],
        geoRestriction: null,
        countires: countires,
        electionType: null,
        candidates: null,
        description: null,
        state: null,
        contry: null
    }),
    methods: {
        createElection() {
            try {
                let formData = new FormData();
                formData.append('file', this.file);
                formData.append('name', this.name);
                formData.append('description', this.description);
                formData.append('candidates', this.candidates);
                formData.append('type', this.electionType);
                formData.append('geoRestriction', this.geoRestriction);
                formData.append('contry', this.contry);
                formData.append('state', this.state);
                this.$http.post ( 'http://127.0.0.1:5000/add/election', formData ).then(function () {
                });
            }
            catch (error) {
                console.log(error)
            }
        }
    },
    computed: {
        stateArr() {
            return this.countires[this.contry]
        }
    },
    mounted() {
        for (const key in countires) {
        this.countriesArr.push(key)
        }
  }
}
</script>
