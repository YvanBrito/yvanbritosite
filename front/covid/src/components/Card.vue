<template>
  <v-card :loading="isLoading" outlined>
    <v-toolbar
      flat
      v-if="enableToolbar"
    >
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer />
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            target="_blank"
            v-on="on"
            disabled
          >
            <v-icon>mdi-cog-outline</v-icon>
          </v-btn>
        </template>
        <span>Source</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            large
            target="_blank"
            v-on="on"
            @click="con"
          >
            <v-icon>mdi-refresh</v-icon>
          </v-btn>
        </template>
        <span>Refresh</span>
      </v-tooltip>
    </v-toolbar>
    <v-card-text>
      <slot></slot>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'Card',
  props: {
    title: {
      type: String,
      required: true
    },
    enableToolbar: {
      type: Boolean,
      default: true
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    con() {
      console.log("estude")
    }
  }
}
</script>

<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 8px;
  border: 1px solid rgba(219, 233, 245, 0.8);
  border-radius: 8px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
  border-bottom: 1px solid rgba(219,233,245,0.8);;
}
</style>