import {
  Box,
  Button,
  Grid,
  Typography,
  Paper,
  styled,
  useTheme,
  useMediaQuery,
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  DialogContentText,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import React, { useState, useEffect, useRef } from "react";

const buttonSX = {
  marginBottom: 1,
  height: 80,
};

export default function Home() {
  let navigate = useNavigate(); // Navigate to different pages
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down("sm")); // Check if the device is mobile

  return (
    <Box
      bgcolor={"primary.white"}
      p={isMobile ? 1 : 2}
      sx={{ marginLeft: 10, marginRight: 10 }}
    >
      {" "}
      {/* Adjust padding for mobile */}
      <Grid container spacing={1} padding={isMobile ? 5 : 5}>
        <Grid item xs={12} align="center">
          <Typography
            variant="h3"
            sx={{
              marginTop: 0,
              marginBottom: 2,
            }}
          >
            LearnIt
          </Typography>
        </Grid>
      </Grid>
    </Box>
  );
}
