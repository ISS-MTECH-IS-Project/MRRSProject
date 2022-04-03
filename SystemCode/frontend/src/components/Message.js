import { BiBot } from "react-icons/bi";
import Symptom from "./Symptom";

const Message = ({ messageIndex, message, onToggle }) => {
  return (
    <div>
      <div className="lc-massage-bot">
        <div className="lc-massage-bot-left">
          <div className="lc-massage-bot-icon">
            <BiBot />
          </div>
        </div>
        <div className="lc-massage">
          <div role="row">
            <div className="lc-massage-left">
              <div
                role="gridcell"
                className="lc-massage-grid-left"
                tabIndex="-1"
              >
                <div>
                  <div className="lc-massage-title-left">
                    <span className="lc-massage-title">ChatBot </span>
                    <span className="lc-massage-title">21:25</span>
                  </div>
                </div>
                <div className="lc-massage-body-left">
                  <div className="lc-massage-body">
                    <span className="Linkify">
                      Want to see what I can do? 🤖
                    </span>
                    {/* Empty symptoms if display of symptoms is undesired */}
                    {message.hasOwnProperty("symptoms") && (
                      <Symptom
                        symptoms={message.symptoms}
                        messageIndex={messageIndex}
                        onToggle={onToggle}
                      ></Symptom>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* user */}
      <div className="lc-massage-user">
        <div className="lc-massage">
          <div role="row">
            <div className="lc-massage-right">
              <div
                role="gridcell"
                className="lc-massage-grid-right"
                tabIndex="-1"
              >
                <div>
                  <div className="lc-massage-title-right">
                    <span className="lc-massage-title">Visitor </span>
                    <span className="lc-massage-title">21:30</span>
                  </div>
                </div>
                <div className="lc-massage-body-right">
                  <div className="lc-massage-body">
                    <span className="Linkify">hi</span>
                  </div>
                </div>
                <div className="lc-massage-read">Read</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Message;
