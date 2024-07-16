import React, { useState } from 'react'
import './Contact.css'

const Contact = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form Submitted:', { name, email, message });
  };

  return (
    <div className='contact-container'>
      <h1>Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <div className='form-group'>
          <label htmlFor="name">Name:</label>
          <input 
          type="text"
          id='name'
          value={name}
          onChange={(e) => setName(e.target.value)}
          required 
          />
        </div>
        <div className='form-group'>
          <label htmlFor="email">Email</label>
          <input 
          type="email"
          id='email'
          value={email}
          onClick={(e) => setEmail(e.target.value)}
          required 
          />
        </div>
        <div className='form-group' id='message'>
          <label htmlFor="message">Message:</label>
          <textarea
          id="message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          required
          ></textarea>
        </div>
        <button type='submit'>Submit</button>
        </form>
    </div>
  )
}

export default Contact
