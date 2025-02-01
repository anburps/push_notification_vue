<template>
  
   <div class="container">
    <h1>Firebase Push Notifications</h1>
    <button @click="enableNotifications">Enable Notifications</button>
  </div>
</template>

<script>
import { requestNotificationPermission } from "./NotificationService";

export default {
  methods: {
    enableNotifications() {
      requestNotificationPermission();
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
