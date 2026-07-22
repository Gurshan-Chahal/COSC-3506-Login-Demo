import { useState } from "react";
import { login } from "./api";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const result = await login(email.trim(), password.trim());
    setMessage(result.message);
  }

  return (
    <div className="container">
      <div className="card">
        <h1>Login Demo</h1>

        <form onSubmit={handleSubmit}>

          <label>Email</label>

          <input
            type="email"
            placeholder="student@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            maxLength={50}
            minLength={12}
            required
          />

          <label>Password</label>

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            maxLength={50}
            minLength={8}
            required
          />

          <button type="submit">
            Login
          </button>

        </form>

        <p
          className={
            message === "Login successful"
              ? "success"
              : "error"
          }
        >
          {message}
        </p>

      </div>
    </div>
  );
}

export default Login;