import React, { useState } from "react";
import "./LoginRegister.css";
import { Link, useNavigate } from "react-router-dom";

const Register = () => {
	const navigate = useNavigate()
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    // const toggleMode = () => {
    //     setUsername("");
    //     setEmail("");
    //     setPassword("");
    //     setConfirmPassword("");
	// };
	const submitForm = (e) => {
		e.preventDefault()
		console.log("Submitted")
		console.log(username, password, confirmPassword, email)
		navigate('/login')
	}

    return (
        <div className="form">
            <div className="logo"></div>
            <div className="login-signup-container">
                <h1>Register with us today!.</h1>
                <form onSubmit={submitForm}>
                    <div className="form-group">
                        <label htmlFor="username">Username:</label>
                        <input
                            type="text"
                            id="username"
							value={username}
							placeholder="Enter Username"
							name="username"
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="email">Email:</label>
                        <input
                            type="email"
							id="email"
							placeholder="Enter Email"
							name="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
							id="password"
							placeholder="Enter Password"
							name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Confirm Password:</label>
                        <input
                            type="password"
							id="confirmPassword"
							placeholder="Confirm Password"
							name="confirmPassword"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            required
                        />
                    </div>

                    <button type="submit">Register</button>
                </form>
                <p className="mt-3">
                    Already have an account?
                    <Link className=" text-red-500 italic" to="/login">
                        Login
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default Register;
