/*
 * The parameter menu component.
 */

import { Menu as AntMenu, Image } from "antd";
import React from "react";
import { useContext } from "react";
import { CountryContext } from "../../../countries";

const { SubMenu } = AntMenu;

export default function Menu(props) {
  const country = useContext(CountryContext);
  function addMenuEntry(parameter, parent) {
    // This function is needed because the menu entries need
    // to be direct descendents of the menu component.
    let children = [];
    for (let child in parameter) {
      const name = parent + "/" + child;
      let logo;
      if (country.organisations && child in country.organisations) {
        logo = (
          <Image
            src={country.organisations[child].logo}
            preview={false}
            height={30}
            width={30}
          />
        );
      } else {
        logo = null;
      }
      if (Array.isArray(parameter[child])) {
        children.push(
          <AntMenu.Item icon={logo} key={name}>
            {
              logo 
              ? <div style={{ paddingLeft: 10 }}>{child}</div> 
              : <div style={{lineHeight: "20px", whiteSpace: "normal", height: "auto"}}>{child}</div>
            }
          </AntMenu.Item>
        );
      } else {
        children.push(
          <SubMenu
            icon={logo}
            key={name}
            title={
              logo 
              ? <div style={{ paddingLeft: 10 }}>{child}</div> 
              : <div style={{lineHeight: "20px", whiteSpace: "normal", height: "auto"}}>{child}</div>
            }
          >
            {addMenuEntry(parameter[child], name)}
          </SubMenu>
        );
      }
    }
    return children;
  }
  return (
    <AntMenu
      onClick={(e) => {
        props.selectParameterGroup(e.key);
      }}
      mode="inline"
      defaultOpenKeys={country.defaultOpenParameterGroups}
      defaultSelectedKeys={[country.defaultSelectedParameterGroup]}
      style={{ paddingBottom: 20 }}
    >
      {addMenuEntry(country.parameterHierarchy, "")}
    </AntMenu>
  );
}
