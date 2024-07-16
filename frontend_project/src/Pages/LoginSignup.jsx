import React, { useState } from 'react'
import './LoginSignup.css'

const LoginSignup = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const toggleMode = () => {
    setIsLogin(!isLogin);
    setUsername('');
    setEmail('');
    setPassword('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isLogin) {
      console.log('Logging in:', {username, password});
    } else {
      console.log('Signup:', { username, email, password });
    }
  };

  return (
    <div className='login-signup-container'>
      <h1>{isLogin ? 'Login' : 'Sign up'}</h1>
      <form onSubmit={handleSubmit}>
        <div className='form-group'>
        <label htmlFor="username">Username:</label>
        <input
         type="text"
         id='username'
         value={username}
         onChange={(e) => setUsername(e.target.value)}
         required 
         />
        </div>
        {!isLogin &&(
          <div className='form-group'>
            <label htmlFor="email">Email:</label>
            <input
             type="text" 
             id='email'
             value={email}
             onChange={(e) => setEmail(e.target.value)}
             required
             />

          </div>
        )}
        <div className='form-group'>
          <label htmlFor="password">Password:</label>
          <input 
          type="text" 
          id='password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          />
        </div>
        <button type='submit'>
          {isLogin ? 'Login' : 'Signup'}</button>
          </form>
          <button onClick={toggleMode}>
            {isLogin ? 'Switch to Sign up' : 'Switch to Login'}

          </button>
          </div>
    
  );
};

export default LoginSignup;
