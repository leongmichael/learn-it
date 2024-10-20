import {
  Box,
  Typography,
  useTheme,
  useMediaQuery,
  TextField,
  IconButton,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import React, { useState, useEffect, useRef } from "react";
// import { ArrowForward } from 'lucide-react';

export default function Home() {
  let navigate = useNavigate(); // Navigate to different pages
  const theme = useTheme();

  const [prompt, setPrompt] = useState("");

  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const apiUrl = `http://127.0.0.1:8000/prompt/${encodeURIComponent(prompt)}`;

    try {
      const response = await fetch(apiUrl, {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log(data); // Process the response data as needed
    } catch (error) {
      console.error('There has been a problem with your fetch operation:', error);
    }
  };



  return (
    <Box
      sx={{
        height: "100vh",
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        pt: 8,
        px: 3,
        backgroundColor: "#fff",
      }}
    >
      <Box
        sx={{
          mb: 8,
          textAlign: "center",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          width: "100%",
          maxWidth: "600px",
        }}
      >
        <Typography
          variant="h2"
          sx={{
            fontSize: { xs: "56px", sm: "72px" },
            fontWeight: 700,
            color: "#7235FF",
            mb: 1,
            letterSpacing: "-0.02em",
            width: "100%",
          }}
        >
          LearnIt
        </Typography>
        <Typography
          variant="h5"
          sx={{
            fontSize: "24px",
            fontWeight: 400,
            color: "#000",
            width: "100%",
          }}
        >
          Learn through generative AI video content.
        </Typography>
      </Box>

      <Box
        sx={{
          display: "flex",
          alignItems: "center",
          width: "100%",
          maxWidth: "600px",
          gap: 1,
          marginTop: -5,
        }}
      >
        <TextField
          fullWidth
          placeholder="What do you want to learn about?"
          variant="outlined"
          onChange={handlePromptChange}
          sx={{
            "& .MuiOutlinedInput-root": {
              borderRadius: "50px",
              backgroundColor: "#fff",
              "& fieldset": {
                borderColor: "#e0e0e0",
              },
              "&:hover fieldset": {
                borderColor: "#4267B2",
              },
            },
          }}
        />
        <IconButton
          sx={{
            backgroundColor: "#7235FF",
            borderRadius: "50%",
            width: "56px",
            height: "56px",
            "&:hover": {
              backgroundColor: "#5225BC",
            },
          }}
          onClick={handleSubmit}
        >
          {/* <ArrowForward color="white" size={24} /> */}
          
        </IconButton>
      </Box>
    </Box>
  );
}
