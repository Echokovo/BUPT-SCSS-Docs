import java.time.LocalDateTime;
/*
 * hh:hour
 * mm:minute
 * state:
 *     false -> 24H_state
 *     true  -> 12H_state
 */
public class Timer{
        private int hour,minute;
        private boolean state;
        public Timer(){
            LocalDateTime ldt=LocalDateTime.now();
            hour=ldt.getHour();
            minute=ldt.getMinute();
        }
        public Timer(int hour,int minute){
            this.hour=hour;
            this.minute=minute;
            this.state=false;
        }
        public Timer(int hour,int minute,boolean state){
            this.hour=hour;
            this.minute=minute;
            this.state=state;
        }
        public int getHour(){
            return hour;
        }
        public int getMinute(){
            return minute;
        }
        public void addHour(){
            addHour(1);
        }
        public void addHour(int h){
            hour+=h;
            hour%=24;
        }
        public void addMinute(){
            addMinute(1);
        }
        public void addMinute(int m){
            minute+=m;
            minute%=60;
        }
        public String toString(){
            if(state){
                return hour%12+":"+minute+(hour<12?"AM":"PM");
            }else{
                return hour+":"+minute;
            }
        }
    }