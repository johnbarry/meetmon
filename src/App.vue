<template>
  <div id="nav">
    <router-link to="/">Meeting</router-link> |
    <router-link to="/dashboard">Dashboard</router-link>
  </div>
  <router-view />
</template>

<style>
h1 {
  color: blue;
  font-family: "Courier New", Courier, monospace;
  font-size: larger;
}

h2 {
  color: blue;
  font-family: "Courier New", Courier, monospace;
  font-size: large;
}

td {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: normal;
  white-space: pre;
  text-align: left;
  border-spacing: 100px;
}

th {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: normal;
  border-spacing: 100px;
  background-color: lightgrey;
  text-decoration: underline;
}
</style>
