package clock;

import clock.Net;
import clock.enums.LogLevel;
import clock.enums.Signal;

public class Main {

	public static void main(String args[]) {

		Net net = Net.getInstance();
		net.logLevel = LogLevel.DEBUG;

		net.sendSignal(Signal.SB);
	}
}

// TODO: populate graph
// TODO: use factory for nodes?
