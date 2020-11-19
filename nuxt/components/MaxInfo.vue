<template>
  <div class="info-container" :class="{ 'info-container--show': show }">
    <v-card width="250">
      <v-card-title class="justify-center">Highest Value</v-card-title>
      <v-divider class="mx-16"></v-divider>
      <v-card-text>
        <h3 class="text-center">{{ maxInfo.country }}</h3>
        <h4 class="text-center">{{ maxInfo.max }}</h4>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  computed: {
    maxInfo() {
      return this.$store.state.maxInfo
    },

    show() {
      return this.$store.state.showMaxInfo
    },
  },
}
</script>

<style lang="scss" scoped>
.info-container {
  position: absolute;
  top: 30px;
  right: 30px;
  z-index: 1;
  transform: translateX(280px);
  transition: 1s ease;

  &--show {
    transform: translateX(0);
  }
}
</style>