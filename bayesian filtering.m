function SimpleRobotWithBayesRule()

format compact

obstacleMap =flipud(...
    [1, 1, 1, 1, 1, 1, 1, 1;
    1, 1, 1, 1, 1, 0, 1, 1;
    1, 0, 0, 0, 0, 0, 0, 1;
    1, 1, 0, 1, 1, 1, 0, 1;
    1, 0, 0, 0, 0, 0, 0, 1;
    1, 1, 1, 1, 1, 1, 1, 1;]);

belief = zeros(size(obstacleMap)); % the belief is the probability that the robot is at any given location

[freespacey,freespacex] = find(obstacleMap == 0);
numFreeSpaces = numel(freespacey);
probs = ones(numFreeSpaces,1)/numFreeSpaces; %uniformly distributed
for i1 = 1:numFreeSpaces
    belief(freespacey(i1),freespacex(i1)) = probs(i1);
end

probStraight = 0.6;
profOffby90Deg = 0.1;

sTruePositive = 0.8;
sTrueNegative = 0.6;

robotInd = ceil(rand*numFreeSpaces); %robot position drawn from a uniform distribution
posRobot = [freespacex(robotInd),freespacey(robotInd)];
posRobot = [3,2];
bShowRobot = 'off'; 

[hWorldFig,hProb] = drawWorld();
[hRobotPos,hRobotOrient] = drawRobot();
titleString = {'''s'' to scan for walls, arrow keys to move,''h'' to hide/unhide robot'; ''};
title(titleString);
axis equal
axis tight
set(figure(1) ,'KeyPressFcn',@keyhandler,'Name','Bayesian Update');

    function [hWorldFig,hProb] = drawWorld()
        figure(1)
        colormap(gray)
        hWorldFig = imagesc(belief);
        set(gca,'YDir','normal');
        [obsy,obsx] = find(obstacleMap == 1);
        for i = 1:numel(obsy)
            rectangle('Position',[obsx(i)-.5,obsy(i)-.5,1,1],'FaceColor','b')
        end
        hProb = zeros(size(belief));
        
        for y = 1:size(belief,1)
            for x = 1:size(belief,2)
                hProb(y,x)=text(x-.4,y,[num2str(100*belief(y,x)),'%']);
            end
        end
        
    end

    function [hRobotPos,hRobotOrient] = drawRobot()
        hRobotPos = rectangle('Position',[posRobot(1)-.5,posRobot(2)-.5,1,1],'Curvature',[1,1],...
            'EdgeColor','r', 'LineWidth',3,'Visible',bShowRobot);
        hRobotOrient = line(posRobot(1)+[0,0.6],posRobot(2)+[0,0],'color','r', 'LineWidth',3,'Visible',bShowRobot);
    end

    function redrawRobot()
        set(hRobotPos,'Position',[posRobot(1)-.5,posRobot(2)-.5,1,1],'Visible',bShowRobot);
        set(hRobotOrient,'XData',posRobot(1)+[0,0.6],'YData',posRobot(2)+[0,0],'Visible',bShowRobot);
    end
    function redrawWorld()
        set(hWorldFig,'CData',belief);
        for y = 1:size(belief,1)
            for x = 1:size(belief,2)
                set(hProb(y,x),'String',[num2str(100*belief(y,x),'%2.2f\n'),'%']);
            end
        end
        %display(['Total probability = ',num2str(sum(sum(belief)))])
    end

    function keyhandler(src,evnt) %#ok<INUSL>
        if strcmp(evnt.Key,'s')
            scan = MeasureScan(posRobot, obstacleMap);
            % the measurement update, line 4 "Algorithm Bayes_filter" of Table
            % 2.1 on page 27 of Probabilistic Robotics.
            for i2 = 1:numFreeSpaces %for each freespace
                oldProb = belief(freespacey(i2),freespacex(i2));
                newProb = BayesianUpdateScan(oldProb, scan, [freespacex(i2),freespacey(i2)]);
                belief(freespacey(i2),freespacex(i2)) = newProb;
            end
            %The resulting belief is usually not a probability
            %distribution (doesn't sum to one) and needs to be nomalized.
            normalizer = 1/sum(sum(belief));
            belief = belief*normalizer;
            titleString{2} = [titleString{2}, 's,'];
        elseif strcmp(evnt.Key,'h')
            if strcmp(bShowRobot,'off')
                bShowRobot = 'on';
            else
                bShowRobot = 'off';
            end
            redrawRobot();
        else
            move = [0,0];
            if strcmp(evnt.Key,'leftarrow')
                move =-[1,0];
                titleString{2} = [titleString{2}, '<,'];
            elseif strcmp(evnt.Key,'rightarrow')
                move = [1,0];
                titleString{2} = [titleString{2}, '>,'];
            elseif strcmp(evnt.Key,'uparrow')
                move = [0,1];
                titleString{2} = [titleString{2}, '\^,'];
            elseif strcmp(evnt.Key,'downarrow')
                move =-[0,1];
                titleString{2} = [titleString{2}, 'v,'];
            end
            if sum(move ~=0)
                % move the robot
                posRobot = moveRobot(posRobot, move, obstacleMap);
                redrawRobot();
                % the movement update (or 'prediction'), line 3 "Algorithm Bayes_filter" Table
                % 2.1 on page 27 of Probabilistic Robotics.
                %for each freespace
                newBelief = zeros(size(belief));
                for i2 = 1:numFreeSpaces
                    %update probabilities at positions around freespacex(i2),freespacey(i2)
                    curPos = [freespacex(i2),freespacey(i2)];
                    px = belief(curPos(2),curPos(1));
                    pMoveS = 0; pMoveR = 0; pMoveL = 0;
                    posS = curPos+move;
                    if( obstacleMap(posS(2), posS(1)) == 0)
                        pMoveS = probStraight;
                        newBelief(posS(2),posS(1)) = newBelief(posS(2),posS(1)) + pMoveS*px;
                    end
                    posR = curPos+[-move(2),move(1)];
                    if( obstacleMap(posR(2), posR(1)) == 0)
                        pMoveR = profOffby90Deg;
                        newBelief(posR(2),posR(1)) = newBelief(posR(2),posR(1)) + pMoveR*px;
                    end
                    posL = curPos+[move(2),-move(1)];
                    if( obstacleMap(posL(2), posL(1)) == 0)
                        pMoveL = profOffby90Deg;
                        newBelief(posL(2),posL(1)) = newBelief(posL(2),posL(1)) + pMoveL*px;
                    end
                    pNoMove = 1-(pMoveS+pMoveR+pMoveL);
                    newBelief(curPos(2),curPos(1)) = newBelief(curPos(2),curPos(1)) + pNoMove*px;
                end
                % update belief according to move
                belief = newBelief;
            end
        end
        %redrawmap
        redrawWorld();
        title(titleString);
    end

    function newProb = BayesianUpdateScan(oldProb, scan, pos)
        %P(x|s) = P(s|x)P(x);
        %       = P(s_right|x)*P(s_up|x)*P(s_left|x)*P(s_down|x)*P(x)
        newProb = ProbOfScanGivenPosition(scan(1), pos +[1,0] ) *...
            ProbOfScanGivenPosition(scan(2), pos +[0,1] ) * ...
            ProbOfScanGivenPosition(scan(3), pos +[-1,0] ) * ...
            ProbOfScanGivenPosition(scan(4), pos +[0,-1] ) * ...
            oldProb;
    end

    function p = ProbOfScanGivenPosition(scan, pos)
        isWall = obstacleMap(pos(2), pos(1));
        if isWall
            if scan
                p = sTruePositive;
            else
                p = 1- sTruePositive;
            end
        else
            if scan
                p = 1-sTrueNegative;
            else
                p = sTrueNegative;
            end
        end
    end

    function scanOut = MeasureScan(pos, obstacleMap)
        scanOut = [
            detectWall(obstacleMap, pos+[1,0]);
            detectWall(obstacleMap, pos+[0,1]);
            detectWall(obstacleMap, pos+[-1,0]);
            detectWall(obstacleMap, pos+[0,-1])
            ];
    end

    function bDetectWall = detectWall(obstacleMap, pos)
        isWall = obstacleMap(pos(2), pos(1));
        
        if isWall
            bDetectWall = (rand() < sTruePositive); % probability of true positive
        else
            bDetectWall = (rand() > sTrueNegative); %probability of true negative
        end
    end

    function posOut = moveRobot(posIn, move, obstacleMap)
        rVal = rand(); %number between 0 and 1
        if rVal< (1-probStraight - 2*profOffby90Deg);
            move = [0,0];
        elseif rVal < (1-probStraight - profOffby90Deg)
            move = [-move(2),move(1)]; %move +90deg of command
        elseif rVal < (1-probStraight)
            move = [move(2),-move(1)]; %move -90deg of command
        end
        
        posOut = posIn + move;
        if( obstacleMap(posOut(2), posOut(1)) ~= 0)
            posOut = posIn; %don't allow collisions.
        end
    end
end