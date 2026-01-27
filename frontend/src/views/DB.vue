<template>
  <div style="padding:24px">
    <h2>DB Query (Admin only)</h2>
    <el-input type="textarea" v-model="sql" rows="6" />
    <el-button @click="run">Run</el-button>
    <pre>{{ result }}</pre>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import api from '../api/axios'
const sql = ref('SELECT 1')
const result = ref(null)
async function run() {
  const res = await api.post('/api/db/query', { sql: sql.value })
  result.value = res.data
}
</script>
