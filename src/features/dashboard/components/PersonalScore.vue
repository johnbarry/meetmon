<script>
export default {
  data() {
    return {
      user: 'john.doe@company.com',
      search: '',
      ranks: [
        {
          rank: 1,
          name: 'Giacomo Guilizzoni',
          email: 'giacomo.guilizzoni@company.com',
          voteCount: 113,
          score: 95.5
        }
      ]
    }
  },
  computed: {
    filteredItems() {
      return this.ranks.filter(item => {
         return item.email.toLowerCase().indexOf(this.search.toLowerCase()) > -1 || item.email === this.user
      })
    }
  }
}
</script>

<template>
  <div class="container">
    <h2>Your Score</h2>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  max-width: 600px;
}
</style>