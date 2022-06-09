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
        },
        {
          rank: 2,
          name: 'Marco Botton',
          email: 'marco.botton@company.com',
          voteCount: 234,
          score: 94.3
        },
        {
          rank: 3,
          name: 'Mariah Macichian',
          email: 'mariah.macichian@company.com',
          voteCount: 164,
          score: 93.1
        },
        {
          rank: 4,
          name: 'Valerie Liberty',
          email: 'valerie.liberty@company.com',
          voteCount: 243,
          score: 92.0
        },
        {
          rank: 5,
          name: 'Christian Halo',
          email: 'christian.halo@company.com',
          voteCount: 243,
          score: 91.4
        },
        {
          rank: '...',
          name: '...',
          email: '...',
          score: '...'
        },
        {
          rank: 521,
          name: 'John Doe',
          email: 'john.doe@company.com',
          voteCount: 134,
          score: 55.6
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
  <h2>Leaderboard</h2>
  <div class="container">
    <div class="filter">
      <div>
        <label>Start date: </label>
        <input type="date" id="start" value="2022-04-10">
      </div>
      <div>
        <input type="text" class="search" placeholder="search people" v-model="search">
      </div>
    </div>
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Name</th>
          <th>Meeting Score</th>
          <th>Votes</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.email" :class="{ active: item.email === user }">
          <td>{{ item.rank }}</td>
          <td>
            {{ item.name }}
            <span v-if="item.rank === 1">🥇</span>
            <span v-if="item.rank === 2">🥈</span>
            <span v-if="item.rank === 3">🥉</span>
          </td>
          <td class="cell-score">{{ item.score }}</td>
          <td>{{ item.voteCount }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin-bottom: 2rem;
}

.filter {
  display: flex;
  justify-content: right;
  margin-bottom: .5rem;
}

.filter div+div {
  margin-left: .5rem;
}

.cell-score {
  text-align: right;
}

td {
  padding: 0.25rem;
}

tr.active td {
  background: lightblue;
}

.search {
  background-image: url('data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNDkwLjQgNDkwLjQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDQ5MC40IDQ5MC40OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+DQo8Zz4NCgk8cGF0aCBkPSJNNDg0LjEsNDU0Ljc5NmwtMTEwLjUtMTEwLjZjMjkuOC0zNi4zLDQ3LjYtODIuOCw0Ny42LTEzMy40YzAtMTE2LjMtOTQuMy0yMTAuNi0yMTAuNi0yMTAuNlMwLDk0LjQ5NiwwLDIxMC43OTYNCgkJczk0LjMsMjEwLjYsMjEwLjYsMjEwLjZjNTAuOCwwLDk3LjQtMTgsMTMzLjgtNDhsMTEwLjUsMTEwLjVjMTIuOSwxMS44LDI1LDQuMiwyOS4yLDBDNDkyLjUsNDc1LjU5Niw0OTIuNSw0NjMuMDk2LDQ4NC4xLDQ1NC43OTZ6DQoJCSBNNDEuMSwyMTAuNzk2YzAtOTMuNiw3NS45LTE2OS41LDE2OS41LTE2OS41czE2OS42LDc1LjksMTY5LjYsMTY5LjVzLTc1LjksMTY5LjUtMTY5LjUsMTY5LjVTNDEuMSwzMDQuMzk2LDQxLjEsMjEwLjc5NnoiLz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjwvc3ZnPg0K');
  background-repeat: no-repeat;
  background-position: right 4px center;
  background-size: 12px;
}
</style>