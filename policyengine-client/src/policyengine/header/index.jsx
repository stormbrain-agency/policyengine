import { Route, Routes } from "react-router-dom";
import MainNavigation from "./mainNavigation";

export function Header(props) {
  let navigation;
  if (props.title || props.noTabs) {
    navigation = <MainNavigation title={props.title} noTabs={props.noTabs} />;
  } else {
    navigation = (
      <Routes>
        <Route path={`policy`} element={<MainNavigation selected="policy" />} />
        <Route
          path={`population-impact`}
          element={<MainNavigation selected="population-impact" />}
        />
        <Route
          path={`household`}
          element={<MainNavigation selected="household" />}
        />
        <Route path={`api-explorer/*`} element={<MainNavigation noTabs />} />
        <Route
          path={"/"}
          element={<MainNavigation selected={window.location.pathname} />}
        />
      </Routes>
    );
  }
  return (
    <div
      style={{
        backgroundColor: "#2c6496",
        position: "sticky",
        top: 0,
        width: "100vw",
        zIndex: 10,
      }}
    >
      {navigation}
    </div>
  );
}
