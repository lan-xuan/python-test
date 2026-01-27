import React, { useEffect, useState } from 'react'
import { fetchItems, createItem } from './api'

export default function App() {
  const [items, setItems] = useState([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  useEffect(() => {
    load()
  }, [])

  async function load() {
    const data = await fetchItems()
    setItems(data)
  }

  async function handleSubmit(e) {
    e.preventDefault()
    if (!title) return
    await createItem({ title, description })
    setTitle('')
    setDescription('')
    load()
  }

  return (
    <div style={{ padding: 24, fontFamily: 'Arial, sans-serif' }}>
      <h1>Items</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: 16 }}>
        <input
          placeholder="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ marginRight: 8 }}
        />
        <input
          placeholder="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{ marginRight: 8 }}
        />
        <button type="submit">Create</button>
      </form>

      <ul>
        {items.map((it) => (
          <li key={it.id}>
            <strong>{it.title}</strong>: {it.description}
          </li>
        ))}
      </ul>
    </div>
  )
}