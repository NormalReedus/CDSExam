<template>
  <div class="container">
    <World />
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'CDS Index',
    }
  },
}
</script>

<style lang="scss">
.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
