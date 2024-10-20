import { ThemeProvider, createTheme } from "@mui/material";
import { Suspense } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Home from "./pages/Home.js";
import NotFound from "./pages/NotFound.js";

const theme = createTheme({
  typography: {
    fontFamily: '"Open Sans", sans-serif',
    button: {
      textTransform: "none",
      fontSize: "medium",
    },
  },

});

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Suspense>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/*" element={<NotFound />} />
          </Routes>
        </Suspense>
      </BrowserRouter>
    </ThemeProvider>
  );
}
