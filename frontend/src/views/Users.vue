<template>
  <div style="padding:24px">
    <h2>Users</h2>
    <el-button type="primary" @click="load">Reload</el-button>
    <el-table :data="users" style="width:100%; margin-top:12px">
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="username" label="Username" />
      <el-table-column prop="full_name" label="Full name" />
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/axios'
const users = ref([])
async function load() {
  const res = await api.get('/api/users/')
  users.value = res.data
}
onMounted(load)
</script>
